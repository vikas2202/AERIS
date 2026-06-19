from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def list_incidents():
    return []


@router.post('/')
def create_incident():
    return {'message': 'incident created'}
