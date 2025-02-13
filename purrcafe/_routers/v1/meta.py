from fastapi import APIRouter

from ..._database import File
from ._schemas import Meta

router = APIRouter()


@router.get("/")
def get_meta() -> Meta:
    return Meta(
        lifetime_guest=File.DEFAULT_GUEST_LIFETIME.total_seconds(),
        lifetime=File.DEFAULT_LIFETIME.total_seconds(),
        file_maxsize_guest=File.GUEST_MAX_FILE_SIZE,
        file_maxsize=File.MAX_FILE_SIZE,
    )
