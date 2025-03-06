from langchain.chains.summarize import load_summarize_chain
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

class SummarizationAgent:
    def __init__(self, llm=None):
        """
        Initializes the SummarizationAgent.

        Args:
            llm (langchain.llms.base.LLM): Language model to use.
        """
        self.llm = llm or OpenAI()

    def simplify_legal_text(self, legal_text, target_audience="general public"):
        """
        Simplifies complex legal text into plain language, preserving accuracy.
        """

        prompt_template = f"""You are an expert legal simplifier. Your task is to translate complex legal language into plain, easy-to-understand terms for the {target_audience}.
        Maintain accuracy and avoid misrepresenting the original meaning.

        Original Legal Text:
        {{legal_text}}

        Simplified Explanation:
        """

        prompt = PromptTemplate(template=prompt_template, input_variables=["legal_text"])
        chain = load_summarize_chain(self.llm, chain_type="stuff", prompt=prompt)
        return chain.run(legal_text)
