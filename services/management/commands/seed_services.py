from django.core.management.base import BaseCommand
from services.models import Service


SERVICES = [
    {
        "name": "Aadhaar Services",
        "name_marathi": "आधार सेवा",
        "description": "Aadhaar enrollment, updates, corrections and e-Aadhaar download services for citizens.",
        "documents_required": "1. Proof of Identity (POI) - ओळखीचा पुरावा\n2. Proof of Address (POA) - पत्त्याचा पुरावा\n3. Date of Birth Proof - जन्म तारखेचा पुरावा\n4. Mobile Number (for OTP) - मोबाईल नंबर (OTP साठी)",
        "category": "aadhaar",
    },
    {
        "name": "PAN Card",
        "name_marathi": "पॅन कार्ड",
        "description": "PAN card registration, corrections and new applications for individuals and businesses.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Passport Size Photo - पासपोर्ट साइज फोटो\n3. Date of Birth Proof - जन्म तारखेचा पुरावा\n4. Identity Proof - ओळखीचा पुरावा\n5. Address Proof - पत्त्याचा पुरावा",
        "category": "pan",
    },
    {
        "name": "Voter ID",
        "name_marathi": "मतदान ओळखपत्र",
        "description": "New voter registration, voter ID card application and corrections for eligible citizens.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Passport Size Photo - पासपोर्ट साइज फोटो\n3. Address Proof - पत्त्याचा पुरावा\n4. Date of Birth Proof - जन्म तारखेचा पुरावा\n5. Mobile Number - मोबाईल नंबर",
        "category": "voter",
    },
    {
        "name": "Passport Assistance",
        "name_marathi": "पासपोर्ट सहाय्य",
        "description": "Complete assistance for passport application form filling, document verification and appointment booking.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. PAN Card - पॅन कार्ड\n3. Birth Certificate - जन्म दाखला\n4. Address Proof - पत्त्याचा पुरावा\n5. Passport Size Photo - पासपोर्ट साइज फोटो\n6. 10th Marksheet - १०वी मार्कशीट",
        "category": "passport",
    },
    {
        "name": "Income Certificate",
        "name_marathi": "उत्पन्न प्रमाणपत्र",
        "description": "Official income certificate issuance for government schemes, scholarships and admissions.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Ration Card - राशन कार्ड\n3. Salary Slip / Income Proof - पगार स्लिप\n4. Address Proof - पत्त्याचा पुरावा\n5. Passport Size Photo - पासपोर्ट साइज फोटो\n6. Self Declaration - स्वयंघोषणापत्र",
        "category": "income",
    },
    {
        "name": "Caste Certificate",
        "name_marathi": "जात प्रमाणपत्र",
        "description": "Caste certificate for reserved category benefits in education, employment and government schemes.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Ration Card - राशन कार्ड\n3. Father's Caste Certificate - वडिलांचे जात प्रमाणपत्र\n4. School Leaving Certificate - शाळा सोडल्याचा दाखला\n5. Address Proof - पत्त्याचा पुरावा\n6. Passport Size Photo - पासपोर्ट साइज फोटो",
        "category": "caste",
    },
    {
        "name": "Domicile Certificate",
        "name_marathi": "अधिवास प्रमाणपत्र",
        "description": "Domicile certificate for education admissions, employment and government scheme benefits.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Ration Card - राशन कार्ड\n3. Address Proof - पत्त्याचा पुरावा\n4. Birth Certificate - जन्म दाखला\n5. School Leaving Certificate - शाळा सोडल्याचा दाखला\n6. Passport Size Photo - पासपोर्ट साइज फोटो",
        "category": "domicile",
    },
    {
        "name": "Nationality Certificate",
        "name_marathi": "राष्ट्रीयत्व प्रमाणपत्र",
        "description": "Nationality certificate for passport, government jobs and official documentation.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Ration Card - राशन कार्ड\n3. Electricity Bill - वीज बिल\n4. 10th Certificate - १०वी सनद\n5. Tehsil Domicile Certificate - तहसिल अधिवास\n6. TC - टीसी",
        "category": "nationality",
    },
    {
        "name": "Age Certificate",
        "name_marathi": "वय प्रमाणपत्र",
        "description": "Age certificate for official documentation and government services.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Tehsil Residence Proof - तहसिल रहिवासी\n3. TC - टीसी\n4. Certificate - सनद\n5. Father's Documents - वडिलांचे कागदपत्र\n6. Ration Card - राशन कार्ड",
        "category": "age",
    },
    {
        "name": "EWS (10%) Certificate",
        "name_marathi": "ईडब्ल्यूएस प्रमाणपत्र",
        "description": "Economically Weaker Section (EWS) certificate for 10% reservation benefits.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Ration Card - राशन कार्ड\n3. Electricity Bill - वीज बिल\n4. Income Certificate (1 year) - उत्पन्न प्रमाणपत्र\n5. Self Declaration - स्वयंघोषणापत्र\n6. Pre-1967 Proof - १९६७ पूर्वीचा पुरावा",
        "category": "ews",
    },
    {
        "name": "Non-Criminal (Non-Creamy Layer) Certificate",
        "name_marathi": "नॉन क्रिमिलीयर प्रमाणपत्र",
        "description": "Non-Creamy Layer certificate for OBC category benefits in education and employment.",
        "documents_required": "1. Income Certificate (3 years) - उत्पन्न प्रमाणपत्र\n2. Ration Card - राशन कार्ड\n3. Electricity Bill - वीज बिल\n4. Caste Certificate - जात प्रमाणपत्र\n5. Aadhaar Card - आधार कार्ड\n6. TC - टीसी",
        "category": "non-creamy",
    },
    {
        "name": "Alpabhudharak (Minority) Certificate",
        "name_marathi": "अल्पभुधारक प्रमाणपत्र",
        "description": "Minority community certificate for availing government schemes and benefits.",
        "documents_required": "1. 7/12 Extract - ७/१२ उतारा\n2. Ration Card - राशन कार्ड\n3. Electricity Bill - वीज बिल\n4. Talathi Report - तलाठी अहवाल\n5. Aadhaar Card - आधार कार्ड\n6. Self Declaration - स्वयंघोषणापत्र",
        "category": "minority",
    },
    {
        "name": "30% Women Reservation Certificate",
        "name_marathi": "३०% महिला आरक्षण प्रमाणपत्र",
        "description": "Certificate for 30% women reservation benefits in government schemes and admissions.",
        "documents_required": "1. Application - अर्ज\n2. Aadhaar Card - आधार कार्ड\n3. Voter ID - मतदान कार्ड\n4. TC - टीसी\n5. Father's Documents - वडिलांचे कागदपत्र\n6. Ration Card - राशन कार्ड\n7. 3 Years Income - ३ वर्षांचे उत्पन्न\n8. Husband's Income - पतीचे उत्पन्न\n9. Caste Bond Affidavit - कास्ट बॉण्ड शपथपत्र",
        "category": "women",
    },
    {
        "name": "Farmer Certificate",
        "name_marathi": "शेतकरी प्रमाणपत्र",
        "description": "Farmer certificate for agricultural schemes, subsidies and government benefits.",
        "documents_required": "1. Application - अर्ज\n2. Self Declaration - स्वयंघोषणापत्र\n3. Aadhaar Card - आधार कार्ड\n4. Ration Card - राशन कार्ड\n5. Affidavit - शपथपत्र\n6. 7/12 Extract - ७/१२ उतारा",
        "category": "farmer",
    },
    {
        "name": "Bhumihin Certificate",
        "name_marathi": "भूमिहीन प्रमाणपत्र",
        "description": "Landless certificate for government schemes and benefits.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Ration Card - राशन कार्ड\n3. Talathi Report - तलाठी अहवाल\n4. Self Declaration - स्वयंघोषणापत्र\n5. No 7/12 Certificate - ७/१२ नसल्याचा दाखला",
        "category": "bhumihin",
    },
    {
        "name": "Ration Card (New & Correction)",
        "name_marathi": "राशन कार्ड (नवीन व दुरुस्ती)",
        "description": "New ration card application and corrections for existing ration cards.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Family Member Certificate - कुटुंब सदस्य दाखला\n3. Property Tax Receipt - घरपावती\n4. Electricity Bill - वीज बिल\n5. Family Record - कुटुंब नोंद\n6. Birth Certificate - जन्म दाखला",
        "category": "ration",
    },
    {
        "name": "E-Shram Card",
        "name_marathi": "ई-श्रम कार्ड",
        "description": "Social security registration for unorganized sector workers with E-Shram card issuance.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. Mobile Number - मोबाईल नंबर\n3. Bank Account Details - बँक खाते तपशील\n4. Passport Size Photo - पासपोर्ट साइज फोटो",
        "category": "eshram",
    },
    {
        "name": "7/12 Holding (Digital)",
        "name_marathi": "७/१२ होल्डिंग डिजिटल",
        "description": "Digital 7/12 land record extract and property documents.",
        "documents_required": "1. 7/12 Extract - ७/१२ उतारा\n2. Talathi Map - तलाठी नकाशा\n3. Aadhaar Card - आधार कार्ड",
        "category": "holding",
    },
    {
        "name": "Crop Insurance",
        "name_marathi": "पीक विमा",
        "description": "Pradhan Mantri Fasal Bima Yojana (PMFBY) enrollment and crop insurance assistance for farmers.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. 7/12 Extract - ७/१२ उतारा\n3. Bank Passbook - बँक पासबुक\n4. Sowing Certificate - पेरणी दाखला\n5. Mobile Number - मोबाईल नंबर\n6. Crop Sowing Details - पीक पेरणी तपशील\n7. Land Ownership Proof - जमीन मालकी",
        "category": "crop",
    },
    {
        "name": "Shop Act License",
        "name_marathi": "दुकान कायदा परवाना",
        "description": "Shop Act license registration and renewal for small businesses and shop owners.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. PAN Card - पॅन कार्ड\n3. Rent Agreement - भाडे करार\n4. Shop Photo - दुकानाचा फोटो\n5. Mobile Number - मोबाईल नंबर",
        "category": "shop",
    },
    {
        "name": "Udyog Aadhaar",
        "name_marathi": "उद्योग आधार",
        "description": "Udyog Aadhaar registration for MSME (Micro, Small & Medium Enterprises).",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. PAN Card - पॅन कार्ड\n3. Bank Passbook - बँक पासबुक\n4. Shop Photo - दुकानाचा फोटो\n5. Email ID - ईमेल आयडी\n6. Mobile Number - मोबाईल नंबर",
        "category": "shop",
    },
    {
        "name": "Food License (FSSAI)",
        "name_marathi": "फूड लायसन्स",
        "description": "FSSAI food license registration for food businesses and restaurants.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. NOC - एनओसी\n3. Health NOC - आरोग्य दाखला\n4. Shop Photo - दुकानाचा फोटो\n5. 7/12 Extract - ७/१२ उतारा\n6. Rent Agreement - भाडे करार\n7. Photo - फोटो\n8. Signature - सही",
        "category": "food",
    },
    {
        "name": "Gazette Certificate",
        "name_marathi": "गॅझेट प्रमाणपत्र",
        "description": "Gazette certificate for name change, correction and official announcements.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. PAN Card - पॅन कार्ड\n3. School Leaving / Birth Certificate - शाळा सोडल्याचा दाखला\n4. Application - नाव बदलण्यासाठी अर्ज\n5. Newspaper Cutting - वर्तमानपत्र कात्रण\n6. Witness - साक्षीदार",
        "category": "gazette",
    },
    {
        "name": "RTO Driving Licence",
        "name_marathi": "आरटीओ ड्रायव्हिंग लायसन्स",
        "description": "Driving licence application, renewal and related RTO services.",
        "documents_required": "1. Aadhaar Card - आधार कार्ड\n2. 2 Photos - २ फोटो\n3. Age Proof - वयाचा पुरावा\n4. Blood Group Certificate - रक्तगट दाखला\n5. 10th Marksheet - १०वी मार्कशीट\n6. Learning Licence - लर्निंग लायसन्स\n7. Medical Certificate - वैद्यकीय दाखला",
        "category": "driving",
    },
    {
        "name": "Caste Validity Certificate",
        "name_marathi": "जात वैधता प्रमाणपत्र",
        "description": "Caste Validity Certificate for verification of caste claims in education and jobs.",
        "documents_required": "1. Application - अर्ज\n2. TC - टीसी\n3. Aadhaar Card - आधार कार्ड\n4. 1 Passport Size Photo - १ पासपोर्ट साइज फोटो\n5. Residence Self Declaration - रहिवासी स्वयंघोषणा\n6. Ration Card - राशन कार्ड\n7. Genealogy - वंशावळ",
        "category": "caste",
    },
]


class Command(BaseCommand):
    help = "Seed services data"

    def handle(self, *args, **options):
        # Delete existing services
        Service.objects.all().delete()
        
        # Add new services
        for data in SERVICES:
            Service.objects.create(
                name=data["name"],
                name_marathi=data["name_marathi"],
                description=data["description"],
                documents_required=data["documents_required"],
                category=data["category"],
                is_active=True,
            )
        
        self.stdout.write(
            self.style.SUCCESS(f"Successfully added {len(SERVICES)} services")
        )