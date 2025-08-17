# index.py

import gradio as gr
from model.load_model import load_xgboost_model
from app import create_prediction_function

model = load_xgboost_model()

if model:
    predict_fn = create_prediction_function(model)

    interface = gr.Interface(
        fn=predict_fn,
        inputs=[
            gr.Number(label="CPU (milli cores)", value=5000),
            gr.Number(label="Memory (mib)", value=8192),
            gr.Number(label="Number of GPUs", value=1),
            gr.Number(label="GPU (milli cores)", value=500),
        ],
        outputs="text",
        title="Hourly Turnaround Time Prediction and Time Slot Recommendation (Today and Tomorrow)"
    )

    interface.launch(share=True)
else:
    print("Gradio interface could not be launched because the model was not loaded.")
