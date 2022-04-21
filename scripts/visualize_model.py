import spacy_streamlit
import typer


def main(models: str, default_text: str):
    models = [name.strip() for name in models.split(",")]
    spacy_streamlit.visualize(
        models, default_text, 
        visualizers=["ner", "textcat"], 
        sidebar_title="Drugs NER Model", 
        show_logo = False, 
        sidebar_description="This model was built for the UNODC DMP Project"
        )


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass
