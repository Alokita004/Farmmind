from __future__ import annotations

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import FakeEmbeddings
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from farmmind.app.core.config import settings


def build_knowledge_base() -> Chroma:
    docs = [
        Document(page_content="Rice cultivation requires consistent water management, fertile soil, and timely nitrogen supplementation. Yellowing leaves may indicate nutrient stress or water stress.", metadata={"topic": "rice"}),
        Document(page_content="Wheat crop profitability improves with careful market timing. Staggered sowing and crop rotation can improve resilience and sustainability.", metadata={"topic": "wheat"}),
        Document(page_content="Soil health is improved by rotating crops, reducing excessive nitrogen, and monitoring pH and moisture levels regularly.", metadata={"topic": "soil health"}),
        Document(page_content="Irrigation planning should consider crop stage, rainfall, and soil moisture to avoid waterlogging and drought stress.", metadata={"topic": "irrigation"}),
        Document(page_content="Fertilizer management should focus on crop demand and soil tests. Excessive fertilizer increases cost and can reduce sustainability.", metadata={"topic": "fertilizer"}),
        Document(page_content="Sustainable agriculture requires combining crop rotation, efficient irrigation, low external inputs, and field monitoring.", metadata={"topic": "sustainability"}),
    ]

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)
    if settings.OPENAI_API_KEY:
        embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    else:
        embeddings = FakeEmbeddings(size=768)

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=settings.VECTOR_DB_PATH,
    )
    return vector_store


def search_agricultural_knowledge(query: str, k: int = 3) -> list[str]:
    try:
        vector_store = Chroma(collection_name="farmmind_knowledge", persist_directory=settings.VECTOR_DB_PATH, embedding_function=FakeEmbeddings(size=768))
        results = vector_store.similarity_search(query, k=k)
        return [doc.page_content for doc in results]
    except Exception:
        fallback = [
            "Rice cultivation requires consistent irrigation and nutrient management.",
            "Soil health improves through crop rotation and balanced fertilization.",
            "Sustainable agriculture minimizes water and fertilizer waste while maintaining productivity.",
        ]
        return fallback
