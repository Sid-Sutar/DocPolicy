import gradio as gr
import requests

BASE_URL = "http://127.0.0.1:8000"

# Upload Contract
def upload_contract(file):

    with open(file.name, "rb") as f:

        response = requests.post(
            f"{BASE_URL}/upload-contract",
            files={
                "file": f
            }
        )

    return response.json()


# Ask Questions
def ask_question(contract_id, question):

    response = requests.get(
        f"{BASE_URL}/ask-contract",
        params={
            "contract_id": contract_id,
            "question": question
        }
    )

    return response.json()


# Analyze Risks
def analyze_risks(contract_id):

    response = requests.get(
        f"{BASE_URL}/analyze-risks/{contract_id}"
    )

    return response.json()


# Gradio UI
with gr.Blocks() as app:

    gr.Markdown("# AI Contract Risk Intelligence Agent")

    # Upload Section
    gr.Markdown("## Upload Contract")

    upload_input = gr.File(
        label="Upload PDF Contract"
    )

    upload_output = gr.JSON()

    upload_button = gr.Button(
        "Upload Contract"
    )

    upload_button.click(
        fn=upload_contract,
        inputs=upload_input,
        outputs=upload_output
    )

    # Question Answering
    gr.Markdown("## Ask Questions")

    contract_id_input = gr.Number(
        label="Contract ID",
        precision=0
    )

    question_input = gr.Textbox(
        label="Question"
    )

    answer_output = gr.JSON()

    ask_button = gr.Button(
        "Ask AI"
    )

    ask_button.click(
        fn=ask_question,
        inputs=[
            contract_id_input,
            question_input
        ],
        outputs=answer_output
    )

    # Risk Analysis
    gr.Markdown("## Analyze Risks")

    risk_contract_id = gr.Number(
        label="Contract ID",
        precision=0
    )

    risk_output = gr.JSON()

    risk_button = gr.Button(
        "Analyze Contract Risks"
    )

    risk_button.click(
        fn=analyze_risks,
        inputs=risk_contract_id,
        outputs=risk_output
    )

app.launch()

