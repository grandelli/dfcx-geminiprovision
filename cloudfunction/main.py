from datetime import datetime
from dateutil.relativedelta import relativedelta
import vertexai
from vertexai.preview.generative_models import GenerativeModel, Part

def submit_multimodal_prompt(project_id: str, location: str, image_path: str, prompt: str) -> str:
    # Initialize Vertex AI
    vertexai.init(project=project_id, location=location)
    # Load the model
    multimodal_model = GenerativeModel("gemini-pro-vision")
    # Query the model
    response = multimodal_model.generate_content(
        [
            # Add an example image
            Part.from_uri(image_path, mime_type="image/jpeg"
            ),
            # Add an example query
            prompt,
        ]
    )

    print("Gemini Output: " + response.text)
    return response.text

def check_expiration_date(project_id: str, region: str, file_path: str):
    #  run multimodal prompt
    prompt = "extract the expiration date from the driving license"
    exp_date_str = submit_multimodal_prompt(project_id,region,file_path,prompt)

    # check whether the driving license is still valid based on the expiration date
    exp_date = datetime.strptime(exp_date_str.replace(" ", ""), '%m/%d/%Y')
    now_date = datetime.now()

    if exp_date >= now_date:
        return True

    return False

def check_driver_age(project_id: str, region: str, file_path: str):
    #  run multimodal prompt
    prompt = "extract the date of birth from the driving license"
    dob_str = submit_multimodal_prompt(project_id,region,file_path,prompt)

    # check whether the driver is > 21 years, as requested from some car rental companies
    dob_date = datetime.strptime(dob_str.replace(" ", ""), '%m/%d/%Y')
    now_date = datetime.now()

    difference_in_years = relativedelta(now_date, dob_date).years

    if difference_in_years >= 21:
        return True

    return False

def validate_driving_license(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    req = request.get_json()
    file_path = 'gs://' + str(req["sessionInfo"]["parameters"]["files"][0])

    # CHANGE THESE PARAMS
    project_id = 'your-project-id'
    region = 'your-region'
    
    # check expiration date
    is_exp_date_valid = check_expiration_date(project_id, region, file_path)

    # check minimum driver age
    is_driver_age_valid = check_driver_age(project_id, region, file_path) 

    is_valid = "KO"
    if is_exp_date_valid is True and is_driver_age_valid is True:
        is_valid = "OK"
    elif is_exp_date_valid is False:
        is_valid = "KO_EXP"
    else:
        is_valid = "KO_AGE"
    
    res = {"sessionInfo": {"parameters": {"response": is_valid}} }
    return res
