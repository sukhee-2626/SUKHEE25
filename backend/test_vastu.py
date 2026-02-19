
from vastu_engine import analyze_vastu
import json

data = {
    'kitchen': 'north-west',
    'master bedroom': 'south-west'
}

result = analyze_vastu(data, 'en')
print(json.dumps(result, indent=2))
