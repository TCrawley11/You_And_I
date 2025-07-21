import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
api_key: str = os.getenv("SUPABASE_API_KEY")
supabase_url: str = os.getenv("SUPABASE_URL")

supabase: Client = create_client(
    supabase_url=supabase_url,
    supabase_key=api_key
)