from fastapi import APIRouter

router = APIRouter()


@router.post('/analyze')
def analyze_incident():
    return {
        'summary': 'Emergency report received',
        'severity': 'medium',
        'resources': ['ambulance', 'police'],
    }
