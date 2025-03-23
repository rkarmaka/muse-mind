import torch
from transformers import pipeline, AutoTokenizer


def generate(topic_name=None):
    if topic_name==None:
        ############# MODEL INITIALIZATION #############
        tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
        pipe = pipeline("text-generation", 
                        model="google/gemma-3-1b-it", 
                        tokenizer=tokenizer, 
                        device="cuda:1", 
                        torch_dtype=torch.bfloat16,
                        temperature=2.0)


        ############# RANDOM TOPIC GENERATOR #############
        prompt = f"""
        Suggest one random topic that I can learn topic. Output only the topic name and NOTHING ELSE.

        Example outputs: Quantum entanglement, Photosynthesis, Large Language Models, Partial differential equation, covalent bonds.
        """


        messages = [
        [
        {
        "role": "system",
        "content": [{"type": "text", "text": "You are a friendly and helpful assistant that helps people educate on topics."},]
        },
        {
        "role": "user",
        "content": [{"type": "text", "text": prompt},]
        },
        ],
        ]

        output = pipe(messages, max_new_tokens=50)

        topic_name = output[0][0]["generated_text"][2]["content"]
        print(f"Let's talk about {topic_name}")

    ############# DEFINE SKILL LEVEL #############
    skill_level = "graduate student" # ["kid", "high school", "college", "graduate school"]
    # topic_name = "Astronomy of constellations" # "Compermanetics"
    ############# EDUCATOR #############
    tokenizer = AutoTokenizer.from_pretrained("google/gemma-3-1b-it")
    pipe = pipeline("text-generation", 
                    model="google/gemma-3-1b-it", 
                    tokenizer=tokenizer, 
                    device="cuda:1", 
                    torch_dtype=torch.bfloat16,
                    temperature=0.5)

    prompt = f"""
    Please generate an interesting, bite-sized teaching moment about a {topic_name}, suitable for {skill_level} audiences. It should be:

    1. Educational – teach a real concept, fact, or piece of knowledge.
    2. Engaging – include a fun analogy, surprising fact, or “did you know?” twist.
    3. Clear and concise – no jargon, aim for a ~100-150 word explanation.
    4. Actionable or thought-provoking – end with a quick question, fun challenge, or an idea to explore further.
    5. Each teaching moment should feel like a mini "aha!" experience—something the user can learn from and remember.

    Start telling the story directly and do not include additional text like "Okay, let's talk about blah blah....".
    """


    messages = [
    [
    {
    "role": "system",
    "content": [{"type": "text", "text": "You are a friendly and curious educator whose job is to spark interest and teach something new in under a minute."},]
    },
    {
    "role": "user",
    "content": [{"type": "text", "text": prompt},]
    },
    ],
    ]

    output = pipe(messages, max_new_tokens=2000)

    content = output[0][0]["generated_text"][2]["content"]

    return topic_name, content
