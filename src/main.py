"""
Main application module.
"""
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

from src.config import Config
from src.models.classification import Classification
from src.utils.logger import get_logger

# Load environment variables from .env file
load_dotenv()

# Initialize logger
logger = get_logger("main")


def main():
    """
    Main entry point for the application.
    """
    logger.info(f"Application started in {Config.APP_MODE} mode")

    tagging_prompt = ChatPromptTemplate.from_template(
        """
        Extract the desired information from the following passage.
        Only extract the properties mentioned in the 'Classification' function.
        Passage:
        {input}
        """
    )

    # Initialize chat model
    llm = ChatOllama(
        temperature=0.7, num_predict=1000, model=Config.LLM
    ).with_structured_output(Classification)

    # Run chat model
    inp = "Sono incredibilmente contento di averti conosciuto! Sono sicuro diventeremo buoni amici!"
    prompt = tagging_prompt.invoke({"input": inp})
    response = llm.invoke(prompt)
    logger.info(f"Input to classify: {inp}")
    logger.info(f"Response: {response}")


if __name__ == "__main__":
    main()
