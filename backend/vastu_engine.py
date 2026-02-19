
# Vastu Engine (Enhanced with Structured Data)

def analyze_vastu(data, language='en'):
    score = 50
    suggestions = []
    
    # --- Vastu Knowledge Base ---
    # Structure: Room -> Direction -> { type, weight, en: {problem, impact, remedy}, ta: {problem, impact, remedy} }
    vastu_kb = {
        'kitchen': {
            'north-east': {
                'type': 'defect', 'weight': -20,
                'en': {
                    'problem': 'Kitchen in North-East (Eshan Corner)',
                    'impact': 'Clash of Fire and Water elements. May cause severe health issues, financial losses, and family disputes.',
                    'remedy': 'Keep the kitchen clean. Avoid using it if possible. Paint walls yellow. Install a Jupiter (Guru) Yantra.',
                    'detail': 'The North-East corresponds to the Water element and is the source of cosmic energy (Jaivik Urja). Placing a Fire element (Kitchen) here creates a destructive clash, evaporating the positive energy before it can circulate. This "Vastu Dosha" is associated with neurological issues and continuous financial drainage.'
                },
                'ta': {
                    'problem': 'வடகிழக்கில் சமையலறை (ஈசான்ய மூலை)', 
                    'impact': 'நீர் மற்றும் நெருப்பு முரண்பாடு. தீவிர உடல்நலக் குறைவு மற்றும் பண இழப்பைத் தரும்.', 
                    'remedy': 'தவிர்க்கவும். மஞ்சள் வர்ணம் பூசவும். குரு யந்திரத்தை வைக்கவும்.',
                    'detail': 'வடகிழக்கு நீர் மூலகத்திற்கு உரியது மற்றும் பிரபஞ்ச ஆற்றலின் மூலமாகும். இங்கே நெருப்பு (சமையலறை) வைப்பது அழிவுகரமான முரண்பாட்டை உருவாக்குகிறது, இது நேர்மறை ஆற்றலை ஆவியாக்குகிறது.'
                }
            },
            'south-east': {
                'type': 'good', 'weight': 15,
                'en': {
                    'problem': 'Kitchen in South-East (Agni Corner)', 
                    'impact': 'Excellent placement. Enhances health, cash flow, and family harmony.', 
                    'remedy': 'Cook facing East.',
                    'detail': 'The South-East is ruled by the Fire element (Agni). Placing the kitchen here synchronizes with nature\'s elements, ensuring food is cooked with positive energy. It boosts the digestive fire and brings vitality to the residents.'
                },
                'ta': {
                    'problem': 'தென்கிழக்கில் சமையலறை (அக்னி மூலை)', 
                    'impact': 'சிறந்த இடம். ஆரோக்கியம், பணப்புழக்கம் மற்றும் குடும்ப ஒற்றுமையை மேம்படுத்தும்.', 
                    'remedy': 'கிழக்கு நோக்கி சமைக்கவும்.',
                    'detail': 'தென்கிழக்கு நெருப்பு மூலகத்தால் ஆளப்படுகிறது. இங்கே சமையலறை அமைப்பது இயற்கையின் கூறுகளுடன் ஒத்திசைகிறது, இது குடியிருப்பவர்களுக்கு உயிர்ச்சக்தியைக் கொண்டுவருகிறது.'
                }
            },
            'north-west': {
                'type': 'good', 'weight': 10,
                'en': {
                    'problem': 'Kitchen in North-West (Vayu Corner)', 
                    'impact': 'Good alternative. Promotes social connections.', 
                    'remedy': 'Ensure proper ventilation.',
                    'detail': 'The North-West (Vayu) represents movement and support. A kitchen here is generally good but may lead to increased expenses or guests.'
                },
                'ta': {
                    'problem': 'வடமேற்கில் சமையலறை (வாயு மூலை)', 
                    'impact': 'நல்ல மாற்று இடம். சமூக தொடர்புகளை ஊக்குவிக்கும்.', 
                    'remedy': 'சரியான காற்றோட்டம் தேவை.',
                    'detail': 'வடமேற்கு (வாயு) இயக்கம் மற்றும் ஆதரவை குறிக்கிறது. இங்கே சமையலறை இருப்பது பொதுவான நன்மைகளைத் தரும், ஆனால் செலவுகளை அதிகரிக்கலாம்.'
                }
            },
            'south-west': {
                'type': 'defect', 'weight': -15,
                'en': {
                    'problem': 'Kitchen in South-West (Nairuthi)', 
                    'impact': 'Disrupts stability. May lead to anxiety and digestive issues.', 
                    'remedy': 'Paint walls yellow. Place a yellow stone under the stove.',
                    'detail': 'South-West is the zone of Earth and stability. Fire here burns stability, leading to relationship conflicts and inability to save money.'
                },
                'ta': {
                    'problem': 'தென்மேற்கில் சமையலறை (நிருதி மூலை)', 
                    'impact': 'நிலைத்தன்மை பாதிப்பு. பதற்றம் மற்றும் செரிமான கோளாறுகளைத் தரும்.', 
                    'remedy': 'மஞ்சள் வர்ணம் பூசவும். அடுப்பின் அடியில் மஞ்சள் கல் வைக்கவும்.',
                    'detail': 'தென்மேற்கு பூமி மற்றும் நிலைத்தன்மையின் மண்டலம். இங்கே உள்ள நெருப்பு நிலைத்தன்மையை எரித்து, உறவு முரண்பாடுகள் மற்றும் பணத்தை சேமிக்க இயலாமைக்கு வழிவகுக்கும்.'
                }
            },
            'north': {
                'type': 'defect', 'weight': -15,
                'en': {
                    'problem': 'Kitchen in North (Kuber Sthan)',
                    'impact': 'Burns wealth opportunities. Financial stagnation.',
                    'remedy': 'Place a green plant. Paint walls light green. Shift stove to SE.',
                    'detail': 'North is the zone of Water and Wealth (Kuber). A kitchen (Fire) here evaporates wealth and opportunities, leading to career stagnation and lack of growth.'
                },
                'ta': {
                    'problem': 'வடக்கில் சமையலறை (குபேர ஸ்தானம்)',
                    'impact': 'செல்வ வாய்ப்புகளை எரிக்கும். நிதி தேக்கம்.',
                    'remedy': 'பச்சை செடி வைக்கவும். வெளிர் பச்சை வர்ணம் பூசவும். அடுப்பை தென்கிழக்குக்கு மாற்றவும்.',
                    'detail': 'வடக்கு நீர் மற்றும் செல்வத்தின் மண்டலம் (குபேரன்). இங்கே சமையலறை (நெருப்பு) இருப்பது செல்வம் மற்றும் வாய்ப்புகளை ஆவியாக்குகிறது, இது தொழில் தேக்கத்திற்கு வழிவகுக்கும்.'
                }
            },
            'west': {
                'type': 'average', 'weight': 5,
                'en': {
                    'problem': 'Kitchen in West (Varuna)',
                    'impact': 'Average placement. Good for food business. May cause skin issues.',
                    'remedy': 'Cook facing East or West. Use white or yellow aesthetics.',
                    'detail': 'West is the zone of Gains and Profits. A kitchen here is excellent for chefs or food businesses but can lead to skin allergies or heat issues for family members.'
                },
                'ta': {
                    'problem': 'மேற்கில் சமையலறை (வருணன்)',
                    'impact': 'சராசரி இடம். உணவு இலாபத்திற்கு நல்லது. தோல் பிரச்சனைகளைத் தரலாம்.',
                    'remedy': 'கிழக்கு அல்லது மேற்கு நோக்கி சமைக்கவும். வெள்ளை அல்லது மஞ்சள் நிறங்களைப் பயன்படுத்தவும்.',
                    'detail': 'மேற்கு இலாபத்தின் மண்டலம். இங்கே சமையலறை இருப்பது சமையல்காரர்களுக்கு சிறந்தது, ஆனால் குடும்ப உறுப்பினர்களுக்கு தோல் ஒவ்வாமை அல்லது வெப்ப பிரச்சனைகளை ஏற்படுத்தலாம்.'
                }
            },
            'south': {
                'type': 'defect', 'weight': -10,
                'en': {
                    'problem': 'Kitchen in South (Yama)',
                    'impact': 'Causes mental stress and short temper.',
                    'remedy': 'Paint walls pale red or orange.',
                    'detail': 'South is the zone of Relaxation and Fame. Fire here disrupts peace of mind, leading to high stress, anger issues, and disturbed sleep patterns.'
                },
                'ta': {
                    'problem': 'தெற்கில் சமையலறை (எமன்)',
                    'impact': 'மன அழுத்தம் மற்றும் முன் கோபத்தை உண்டாக்கும்.',
                    'remedy': 'வெளிர் சிவப்பு அல்லது ஆரஞ்சு வர்ணம் பூசவும்.',
                    'detail': 'தெற்கு ஓய்வு மற்றும் புகழின் மண்டலம். இங்கே நெருப்பு இருப்பது மன அமைதியைக் குலைத்து, அதிக அழுத்தம், கோபம் மற்றும் தூக்கமின்மைக்கு வழிவகுக்கும்.'
                }
            },
            'east': {
                'type': 'defect', 'weight': -5,
                'en': {
                    'problem': 'Kitchen in East (Surya)',
                    'impact': 'Minor defect. Can cause mild health issues for women.',
                    'remedy': 'Place a green marble under the stove.',
                    'detail': 'East is the zone of Social Connections. While not a major defect, a kitchen here can sometimes burn social connections or affect the health of the lady of the house.'
                },
                'ta': {
                    'problem': 'கிழக்கில் சமையலறை (சூரியன்)',
                    'impact': 'சிறிய குறைபாடு. பெண்களுக்கு லேசான உடல்நலப் பிரச்சனைகளைத் தரலாம்.',
                    'remedy': 'அடுப்பின் அடியில் பச்சை பளிங்கு கல் வைக்கவும்.',
                    'detail': 'கிழக்கு சமூக தொடர்புகளின் மண்டலம். இது பெரிய குறைபாடு இல்லை என்றாலும், சில நேரங்களில் சமூக உறவுகளை பாதிக்கலாம் அல்லது வீட்டுப் பெண்களின் ஆரோக்கியத்தை பாதிக்கலாம்.'
                }
            }
        },
        'master_bedroom': {
            'south-west': {
                'type': 'good', 'weight': 20,
                'en': {
                    'problem': 'Bedroom in South-West (Nairuthi)', 
                    'impact': 'Best position. Brings stability, leadership, and health.', 
                    'remedy': 'Sleep with head towards South.',
                    'detail': 'The Master Bedroom in the Earth zone (SW) grounds the energy of the head of the family, providing mental peace, quick decision-making power, and authority.'
                },
                'ta': {
                    'problem': 'தென்மேற்கில் படுக்கையறை (நிருதி மூலை)', 
                    'impact': 'சிறந்த இடம். நிலைத்தன்மை, தலைமைத்துவம் மற்றும் ஆரோக்கியம் தரும்.', 
                    'remedy': 'தெற்கு நோக்கி தலை வைத்து தூங்கவும்.',
                    'detail': 'தென்மேற்கு (பூமி) மண்டலத்தில் உள்ள பிரதான படுக்கையறை குடும்பத் தலைவரின் ஆற்றலை நிலைநிறுத்துகிறது, மன அமைதி மற்றும் அதிகாரத்தை வழங்குகிறது.'
                }
            },
            'north-east': {
                'type': 'defect', 'weight': -15,
                'en': {
                    'problem': 'Bedroom in North-East (Eshan)', 
                    'impact': 'Not for couples. Causes health issues and restlessness.', 
                    'remedy': 'Shift room. Use for meditation only.',
                    'detail': 'Calculated as the zone of Water and Divine thoughts. A bedroom here causes an overactive mind, preventing restful sleep and hindering conception for couples.'
                },
                'ta': {
                    'problem': 'வடகிழக்கில் படுக்கையறை (ஈசான்ய மூலை)', 
                    'impact': 'தம்பதிகளுக்கு ஏற்றதல்ல. உடல்நலக் குறைவு மற்றும் ஓய்வின்மையைத் தரும்.', 
                    'remedy': 'அறையை மாற்றவும். தியானத்திற்கு மட்டும் பயன்படுத்தவும்.',
                    'detail': 'நீர் மற்றும் தெய்வீக சிந்தனைகளின் மண்டலம். இங்கே படுக்கையறை இருப்பது மிகையான சிந்தனையைத் தூண்டி, நிம்மதியான தூக்கத்தைத் தடுக்கும்.'
                }
            },
            'south-east': {
                'type': 'defect', 'weight': -10,
                'en': {
                    'problem': 'Bedroom in South-East (Agni)', 
                    'impact': 'Fire zone. Causes aggression and sleep disorders.', 
                    'remedy': 'Use cooling colors (Blue/Green). Avoid Red.',
                    'detail': 'South-East is the zone of Fire. Sleeping here increases body heat and aggression, leading to frequent quarrels and high blood pressure.'
                },
                'ta': {
                    'problem': 'தென்கிழக்கில் படுக்கையறை (அக்னி மூலை)', 
                    'impact': 'நெருப்பு மண்டலம். கோபம் மற்றும் தூக்கமின்மையை உருவாக்கும்.', 
                    'remedy': 'குளிர்ச்சியான நிறங்களை (நீலம்/பச்சை) பயன்படுத்தவும்.',
                    'detail': 'தென்கிழக்கு நெருப்பு மண்டலம். இங்கே தூங்குவது உடல் வெப்பத்தையும் கோபத்தையும் அதிகரிக்கிறது, இது அடிக்கடி சண்டைகள் மற்றும் உயர் இரத்த அழுத்தத்திற்கு வழிவகுக்கும்.'
                }
            },
            'north': {
                'type': 'defect', 'weight': -15,
                'en': {
                    'problem': 'Bedroom in North (Kuber)', 
                    'impact': 'Good for young but bad for couples. No stability.', 
                    'remedy': 'Use for children or study. Avoid as master bedroom.',
                    'detail': 'North is ruled by Mercury and Kuber. While good for career and learning, it lacks the Earth element\'s stability required for the master of the house, leading to restless careers.'
                },
                'ta': {
                    'problem': 'வடக்கில் படுக்கையறை (குபேரன்)', 
                    'impact': 'இளைஞர்களுக்கு நல்லது, தம்பதிகளுக்கு ஏற்றதல்ல. நிலைத்தன்மை இருக்காது.', 
                    'remedy': 'குழந்தைகள் அல்லது படிப்பதற்கு பயன்படுத்தவும். பிரதான படுக்கையறையாக தவிர்க்கவும்.',
                    'detail': 'வடக்கு திசை புதன் மற்றும் குபேரால் ஆளப்படுகிறது. தொழில் மற்றும் கல்விக்கு நல்லது என்றாலும், குடும்பத் தலைவருக்குத் தேவையான பூமியின் நிலைத்தன்மை இங்கு இல்லை.'
                }
            },
            'west': {
                'type': 'good', 'weight': 10,
                'en': {
                    'problem': 'Bedroom in West (Varuna)', 
                    'impact': 'Good for gains and wealth storage.', 
                    'remedy': 'Sleep with head towards South or East.',
                    'detail': 'West is the zone of Gains. A master bedroom here ensures that the efforts put in by the family head result in tangible profits and financial security.'
                },
                'ta': {
                    'problem': 'மேற்கில் படுக்கையறை (வருணன்)', 
                    'impact': 'செல்வம் மற்றும் இலாபத்திற்கு நல்லது.', 
                    'remedy': 'தெற்கு அல்லது கிழக்கு நோக்கி தலை வைத்து தூங்கவும்.',
                    'detail': 'மேற்கு இலாபத்தின் மண்டலம். இங்கே பிரதான படுக்கையறை இருப்பது குடும்பத் தலைவரின் முயற்சிகள் உறுதியான இலாபத்தையும் நிதி பாதுகாப்பையும் தருவதை உறுதி செய்கிறது.'
                }
            },
            'north-west': {
                'type': 'average', 'weight': 5,
                'en': {
                    'problem': 'Bedroom in North-West (Vayu)', 
                    'impact': 'Causes instability and movement. Good for guests.', 
                    'remedy': 'Use white or cream colors.',
                    'detail': 'North-West is the zone of Air/Wind. Sleeping here can cause instability in life or frequent traveling. It is best suited for guest bedrooms or marriageable daughters.'
                },
                'ta': {
                    'problem': 'வடமேற்கில் படுக்கையறை (வாயு)', 
                    'impact': 'நிலையற்ற தன்மை மற்றும் இடத்தை மாற்றும். விருந்தினர்களுக்கு நல்லது.', 
                    'remedy': 'வெள்ளை அல்லது கிரீம் நிறங்களை பயன்படுத்தவும்.',
                    'detail': 'வடமேற்கு காற்று மண்டலம். இங்கே தூங்குவது வாழ்க்கையில் உறுதியின்மை அல்லது அடிக்கடி பயணங்களை ஏற்படுத்தும். இது விருந்தினர் அறை அல்லது திருமண வயதுடைய பெண்களுக்கு ஏற்றது.'
                }
            }
        },
        'toilet': {
            'north-east': {
                'type': 'defect', 'weight': -25,
                'en': {
                    'problem': 'Toilet in North-East (Eshan)', 
                    'impact': 'Critical Defect. Blocks positive energy. Causes severe ruin.', 
                    'remedy': 'Shift immediately. Keep clean and closed. Use sea salt.',
                    'detail': 'North-East is the head of the Vastu Purusha. A toilet here is like applying filth to the head/brain. It causes severe mental issues, brain disorders, and cancer in extreme cases.'
                },
                'ta': {
                    'problem': 'வடகிழக்கில் கழிப்பறை (ஈசான்ய மூலை)', 
                    'impact': 'கடுமையான குறைபாடு. நேர்மறை ஆற்றலைத் தடுக்கும். அழிவைத் தரும்.', 
                    'remedy': 'உடனடியாக மாற்றவும். சுத்தமாக வைக்கவும். கல் உப்பு பயன்படுத்தவும்.',
                    'detail': 'வடகிழக்கு வாஸ்து புருஷனின் தலை. இங்கே கழிப்பறை இருப்பது தலை/மூளையில் அழுக்கை பூசுவது போன்றது. இது கடுமையான மனநல பிரச்சனைகள் மற்றும் மூளை தொடர்பான நோய்களை உண்டாக்கும்.'
                }
            },
            'south-west': {
                'type': 'defect', 'weight': -15,
                'en': {
                    'problem': 'Toilet in South-West (Nairuthi)', 
                    'impact': 'Drains stability and savings. Kidney/Leg issues.', 
                    'remedy': 'Keep door closed. Use yellow tape around the seat.',
                    'detail': 'Since South-West stores wealth and stability, a toilet here drains out all savings and causes instability in career and relationships.'
                },
                'ta': {
                    'problem': 'தென்மேற்கில் கழிப்பறை (நிருதி மூலை)', 
                    'impact': 'சேமிப்பை அழிக்கும். சிறுநீரக/கால் பிரச்சனைகள் வரும்.', 
                    'remedy': 'கதவை மூடி வைக்கவும். ஆசனத்தைச் சுற்றி மஞ்சள் டேப் ஒட்டவும்.',
                    'detail': 'தென்மேற்கு செல்வம் மற்றும் நிலைத்தன்மையை சேமிக்கும் இடம் என்பதால், இங்கே கழிப்பறை இருப்பது அனைத்து சேமிப்புகளையும் வெளியேற்றி, தொழில் மற்றும் உறவுகளில் உறுதியின்மையை ஏற்படுத்தும்.'
                }
            },
            'north-west': {
                'type': 'good', 'weight': 10,
                'en': {
                    'problem': 'Toilet in North-West', 
                    'impact': 'Ideal position. Releases negativity effectively.', 
                    'remedy': 'Ensure ventilation.',
                    'detail': 'North-West (Air element) controls elimination. A toilet here helps in the proper release of toxins from the body and negative emotions from the mind.'
                },
                'ta': {
                    'problem': 'வடமேற்கில் கழிப்பறை', 
                    'impact': 'சரியான இடம். எதிர்மறையை வெளியேற்ற உதவும்.', 
                    'remedy': 'காற்றோட்டத்தை உறுதி செய்யவும்.',
                    'detail': 'வடமேற்கு (காற்று) வெளியேற்றத்தைக் கட்டுப்படுத்துகிறது. இங்கே கழிப்பறை இருப்பது உடலில் இருந்து நச்சுகளையும், மனதிலிருந்து எதிர்மறை உணர்வுகளையும் சரியாக வெளியேற்ற உதவுகிறது.'
                }
            },
            'south-east': {
                'type': 'defect', 'weight': -20,
                'en': {
                    'problem': 'Toilet in South-East (Agni)', 
                    'impact': 'Fire/Water clash. Legal troubles and women\'s health.', 
                    'remedy': 'Correct with Copper strips or red bulbs.',
                    'detail': 'South-East is the direction of Fire. A toilet (Water activity) here extinguishes the fire, leading to digestion issues, legal hassles, and safety concerns for women.'
                },
                'ta': {
                    'problem': 'தென்கிழக்கில் கழிப்பறை (அக்னி)', 
                    'impact': 'நெருப்பு/நீர் முரண்பாடு. சட்ட சிக்கல்கள் மற்றும் பெண்கள் ஆரோக்கியம் பாதிப்பு.', 
                    'remedy': 'செப்பு கம்பி அல்லது சிவப்பு விளக்கு பயன்படுத்தவும்.',
                    'detail': 'தென்கிழக்கு நெருப்பு திசை. இங்கே கழிப்பறை (நீர்) இருப்பது நெருப்பை அணைத்து, செரிமானக் கோளாறுகள், சட்ட சிக்கல்கள் மற்றும் பெண்களின் பாதுகாப்பில் கவலைகளை ஏற்படுத்தும்.'
                }
            },
            'north': {
                'type': 'defect', 'weight': -10,
                'en': {
                    'problem': 'Toilet in North (Kuber)', 
                    'impact': 'Blocks career growth and money flow.', 
                    'remedy': 'Use blue tape. Keep it very clean.',
                    'detail': 'North represents opportunities. A toilet here flushes down opportunities and blocks promotions or new business deals.'
                },
                'ta': {
                    'problem': 'வடக்கில் கழிப்பறை (குபேரன்)', 
                    'impact': 'தொழில் வளர்ச்சி மற்றும் பண வரவை தடுக்கும்.', 
                    'remedy': 'நீல நிற டேப் ஒட்டவும். மிகச் சுத்தமாக வைக்கவும்.',
                    'detail': 'வடக்கு வாய்ப்புகளை குறிக்கிறது. இங்கே கழிப்பறை இருப்பது வாய்ப்புகளை அழித்து, பதவி உயர்வு அல்லது புதிய வணிக ஒப்பந்தங்களை தடுக்கும்.'
                }
            },
            'west': {
                'type': 'good', 'weight': 5,
                'en': {
                    'problem': 'Toilet in West (Varuna)', 
                    'impact': 'Second best option. Generally acceptable.', 
                    'remedy': 'Ensure proper exhaust.',
                    'detail': 'West is the zone of Fulfillment. A toilet here is generally acceptable if the North-West zone is not available, but should be treated if causing lack of fulfillment.'
                },
                'ta': {
                    'problem': 'மேற்கில் கழிப்பறை (வருணன்)', 
                    'impact': 'இரண்டாவது சிறந்த விருப்பம். பொதுவாக ஏற்றுக் கொள்ளத்தக்கது.', 
                    'remedy': 'சரியான காற்றோட்டம் உறுதி செய்யவும்.',
                    'detail': 'மேற்கு நிறைவின் மண்டலம். வடமேற்கு கிடைக்காத பட்சத்தில் இது ஒரு நல்ல மாற்றாகும், ஆனால் அதிருப்தியை ஏற்படுத்தினால் கவனிக்க வேண்டும்.'
                }
            }
        },
        'entrance': {
            'north': {
                'type': 'good', 'weight': 15, 
                'en': {
                    'problem': 'Entrance in North', 
                    'impact': 'Excellent (Kuber Sthan). Brings wealth.', 
                    'remedy': 'Keep clutter-free.',
                    'detail': 'North is ruled by Kuber, the lord of wealth. An entrance here invites abundant financial opportunities and career growth.'
                }, 
                'ta': {
                    'problem': 'வடக்கு வாசல்', 
                    'impact': 'மிகவும் சிறந்தது (குபேர ஸ்தானம்). செல்வம் தரும்.', 
                    'remedy': 'சுத்தமாக வைக்கவும்.',
                    'detail': 'வடக்கு திசை செல்வத்தின் அதிபதியான குபேரால் ஆளப்படுகிறது. இங்கே வாசல் அமைப்பது ஏராளமான நிதி வாய்ப்புகளையும் தொழில் வளர்ச்சியையும் அழைக்கும்.'
                }
            },
            'east': {
                'type': 'good', 'weight': 15, 
                'en': {
                    'problem': 'Entrance in East', 
                    'impact': 'Excellent. Brings fame and health.', 
                    'remedy': 'Keep well-lit.',
                    'detail': 'East is the direction of the rising sun (Surya). An entrance here brings new beginnings, name, fame, and social connections.'
                }, 
                'ta': {
                    'problem': 'கிழக்கு வாசல்', 
                    'impact': 'மிகவும் சிறந்தது. புகழ் மற்றும் ஆரோக்கியம் தரும்.', 
                    'remedy': 'நன்கு வெளிச்சமாக வைக்கவும்.',
                    'detail': 'கிழக்கு உதய சூரியனின் திசை. இங்கே வாசல் அமைப்பது புதிய தொடக்கங்கள், பெயர், புகழ் மற்றும் சமூக தொடர்புகளைக் கொண்டுவரும்.'
                }
            },
            'south-west': {
                'type': 'defect', 'weight': -20, 
                'en': {
                    'problem': 'Entrance in South-West', 
                    'impact': 'Entrance of difficulties and debt.', 
                    'remedy': 'Install Lead Pyramid.',
                    'detail': 'South-West entry allows negative energy to enter and positive energy to leave (Energy leak). It brings struggles, debts, and relationship failures.'
                }, 
                'ta': {
                    'problem': 'தென்மேற்கு வாசல்', 
                    'impact': 'கஷ்டங்கள் மற்றும் கடன்களின் வாசல்.', 
                    'remedy': 'ஈய பிரமிடு வைக்கவும்.',
                    'detail': 'தென்மேற்கு நுழைவாயில் எதிர்மறை ஆற்றலை உள்ளே அனுமதித்து, நேர்மறை ஆற்றலை வெளியேறச் செய்கிறது. இது போராட்டங்கள், கடன்கள் மற்றும் உறவு தோல்விகளைக் கொண்டுவரும்.'
                }
            },
            'south-east': {
                'type': 'defect', 'weight': -15, 
                'en': {
                    'problem': 'Entrance in South-East', 
                    'impact': 'Updates Anxiety and Fire accidents.', 
                    'remedy': 'Paint door Red. Add Copper Swastik.',
                    'detail': 'South-East is the zone of Fire. An entrance here creates excessive fire energy, leading to angry temperament, accidents, and theft.'
                }, 
                'ta': {
                    'problem': 'தென்கிழக்கு வாசல்', 
                    'impact': 'பதற்றம் மற்றும் தீ விபத்துகளை உண்டாக்கும்.', 
                    'remedy': 'கதவுக்கு சிவப்பு வர்ணம் பூசவும். செப்பு ஸ்வஸ்திக் ஒட்டவும்.',
                    'detail': 'தென்கிழக்கு நெருப்பு மண்டலம். இங்கே வாசல் இருப்பது அதிகப்படியான நெருப்பு ஆற்றலை உருவாக்கி, கோபம், விபத்துக்கள் மற்றும் திருட்டுக்கு வழிவகுக்கும்.'
                }
            },
            'north-west': {
                'type': 'average', 'weight': 5, 
                'en': {
                    'problem': 'Entrance in North-West', 
                    'impact': 'Variable placement. Helpful people.', 
                    'remedy': 'Use white colors. Keep clean.',
                    'detail': 'North-West is the zone of Support. An entrance here can bring helpful people into your life but can also make the residents stay away from home frequently.'
                }, 
                'ta': {
                    'problem': 'வடமேற்கு வாசல்', 
                    'impact': 'மாறுபட்ட பலன்கள். உதவும் மனிதர்கள்.', 
                    'remedy': 'வெள்ளை நிறங்களை பயன்படுத்தவும். சுத்தமாக வைக்கவும்.',
                    'detail': 'வடமேற்கு ஆதரவின் மண்டலம். இங்கே வாசல் இருப்பது உதவும் மனிதர்களை ஈர்க்கும், ஆனால் குடியிருப்பவர்களை அடிக்கடி வீட்டை விட்டு வெளியே இருக்கச் செய்யலாம்.'
                }
            },
            'west': {
                'type': 'good', 'weight': 10, 
                'en': {
                    'problem': 'Entrance in West', 
                    'impact': 'Good for Gains. Financial profit.', 
                    'remedy': 'Keep clean. Use metal elements.',
                    'detail': 'West is the zone of Profits (Varun). An entrance here ensures good financial returns and business profits.'
                }, 
                'ta': {
                    'problem': 'மேற்கு வாசல்', 
                    'impact': 'இலாபத்திற்கு நல்லது. நிதி ஆதாயம்.', 
                    'remedy': 'சுத்தமாக வைக்கவும். உலோக பொருட்களை பயன்படுத்தவும்.',
                    'detail': 'மேற்கு இலாபத்தின் மண்டலம். இங்கே வாசல் அமைப்பது நல்ல நிதி வருவாய் மற்றும் வணிக இலாபங்களை உறுதி செய்கிறது.'
                }
            }
        }
    }

    # Helper translations for generic cases
    general_trans = {
        'en': {
            'neutral_title': '{room} in {dir}',
            'neutral_impact': 'Placement has mixed or neutral effects.',
            'neutral_remedy': 'Consult a Vastu expert for specific corrections.',
            'excellent': "Excellent Vastu Compliance! Space has high positive vibrations.",
            'average': "Moderate Vastu Compliance. Improve with simple remedies.",
            'poor': "Critical Vastu Corrections Needed. Energy flow is blocked."
        },
        'ta': {
            'neutral_title': '{dir} திசையில் {room}',
            'neutral_impact': 'இந்த இடம் கலப்பு அல்லது நடுநிலையான பலன்களைத் தரும்.',
            'neutral_remedy': 'குறிப்பிட்ட பரிகாரங்களுக்கு வாஸ்து நிபுணரை அணுகவும்.',
            'excellent': "மிகச்சிறந்த வாஸ்து அமைப்பு! அதிக நேர்மறை அதிர்வுகள் உள்ளன.",
            'average': "மிதமான வாஸ்து அமைப்பு. எளிய பரிகாரங்கள் மூலம் மேம்படுத்தலாம்.",
            'poor': "முக்கியமான வாஸ்து திருத்தங்கள் தேவை. ஆற்றல் ஓட்டம் தடைபட்டுள்ளது."
        }
    }
    
    gt = general_trans.get(language, general_trans['en'])

    # Processing Logic
    for room_key, direction in data.items():
        base_room = room_key.lower().replace(" ", "_").strip()
        base_dir = direction.lower().strip()
        
        # Check if room exists in KB
        found = False
        if base_room in vastu_kb:
            kb_room = vastu_kb[base_room]
            # Check if exact direction exists
            if base_dir in kb_room:
                rule = kb_room[base_dir]
                score += rule['weight']
                content = rule.get(language, rule['en'])
                suggestions.append({
                    "suggestion_type": rule['type'], # 'good', 'defect'
                    "card_title": content['problem'],
                    "impact": content['impact'],
                    "remedy": content['remedy'],
                    "detail": content.get('detail', '') # Add detail logic
                })
                found = True
            else:
                # Direction not explicitly good/bad in KB, usually means neutral or not critical
                pass 
        
        if not found:
            # Add a generic neutral card
            suggestions.append({
                "suggestion_type": "neutral",
                "card_title": gt['neutral_title'].format(room=room_key, dir=direction),
                "impact": gt['neutral_impact'],
                "remedy": gt['neutral_remedy'],
                "detail": ""
            })

    # Final Score Calculation
    final_score = max(0, min(100, score))
    
    if final_score > 80: explanation = gt['excellent']
    elif final_score > 50: explanation = gt['average']
    else: explanation = gt['poor']

    return {
        "score": final_score,
        "suggestions": suggestions, # List of structured dicts
        "explanation": explanation
    }
