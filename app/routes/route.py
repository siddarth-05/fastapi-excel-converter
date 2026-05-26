from fastapi import APIRouter, File, UploadFile, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from services import excelconvert
from dependencies import auth
from fastapi.exceptions import HTTPException
template = Jinja2Templates(directory="templates")
router = APIRouter()
@router.post("/uploadfile/")
async def upload_excel(file: UploadFile = File(...), _: None = Depends(auth.require_api_key)):    
    if file.content_type != "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" and file.content_type != "application/vnd.ms-excel" or file.size == 0:
        raise HTTPException(status_code=400, detail= "Upload Excel (.xls or .xlsx) file only")
    try:     
        resp = excelconvert.convert_excel_to_records(file.file)        
        return JSONResponse(content={
                "success": True,
                "filename": file.filename,
                "size": file.size,
                "type": file.content_type,
                "data": resp
            }, status_code=200)
    except(ValueError):
        raise HTTPException(status_code=400, detail="File Read Error")
@router.get("/")
def home(request:Request):    
    return template.TemplateResponse(request=request,name="index.html")
    

