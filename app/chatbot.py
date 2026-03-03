from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_NAME = "huzaifashahid/mental-health-bot"

_model     = None
_tokenizer = None

def load():
    global _model, _tokenizer
    print("Loading model...")
    _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    _tokenizer.pad_token = _tokenizer.eos_token
    _model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
    print("Model ready!")

def get_response(user_message):
    if not user_message.strip():
        return "I am here to listen. Can you share how you are feeling?"
    if _model is None:
        try:
            load()
        except Exception as e:
            return f"Model load nahi ho saka: {e}"

    prompt = f"User: {user_message.strip()}\nBot:"
    inputs = _tokenizer(prompt, return_tensors="pt", truncation=True, max_length=256)

    with torch.no_grad():
        outputs = _model.generate(
            **inputs,
            max_new_tokens=100,
            temperature=0.7,
            do_sample=True,
            pad_token_id=_tokenizer.eos_token_id,
            repetition_penalty=1.8,
            no_repeat_ngram_size=3
        )

    response = _tokenizer.decode(outputs[0], skip_special_tokens=True)
    if "Bot:" in response:
        response = response.split("Bot:")[-1].strip()
    lines = [l.strip() for l in response.split("\n") if l.strip()]
    return lines[0] if lines else "I am here for you."

def get_status():
    if _model is None:
        try:
            load()
        except Exception as e:
            return {"status": "error", "detail": str(e)}
    return {"status": "ok", "model": MODEL_NAME}