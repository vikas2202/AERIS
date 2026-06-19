from fastapi import APIRouter

router = APIRouter()


@router.post('/register')
def register():
    return {'message': 'registration placeholder'}


@router.post('/login')
def login():
    return {'access_token': 'demo-token', 'token_type': 'bearer'}
