from ninja import NinjaAPI, Schema
from .models import Membro
from typing import List, Optional
from django.contrib.auth import authenticate
from ninja.errors import HttpError
from datetime import date

# Criando a API.
api = NinjaAPI(title="Sistema IPB Cambuhy API")

# SCHEMAS

# Criando o schema para o login. Definindo o formato esperado no POST.
class LoginSchema(Schema):
    username: str
    password: str

# Criando o schema para o membro. POST, GET e PATCH.
class MembroSchema(Schema):
    id: Optional[int] = None # Importante ser opcional, pois no POST o ID não existe.
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    is_lideranca: bool = False

# ROTAS DE AUTENTICAÇÃO

# Rota do POST Login.
@api.post("/login")
def login(request, data: LoginSchema):
    # Valida usuário do DJANGO.
    user = authenticate(username=data.username, password=data.password)
    if user:
        return {
            "token": "token-temporario-de-teste", # Gera token teste.
            "user": {
                "username": user.username, 
                "is_lideranca": user.is_staff
            }
        }
    raise HttpError(401, "Usuário ou senha inválidos")

# ROTAS DE MEMBROS (CRUD)

# Com o método GET. Retorna todos membros cadastrados.
@api.get("/membros", response=List[MembroSchema])
def listar_membros(request):
    return Membro.objects.all()

# Com o método POST. Cria um novo membro.
@api.post("/membros")
def criar_membro(request, data: MembroSchema):
    dados = data.dict(exclude_unset=True)
    dados.pop('id', None)
    
    membro = Membro.objects.create(**dados)
    return {"id": membro.id, "message": "Membro cadastrado com sucesso"}

# Com o método PATCH. Edita um membro existente.
@api.patch("/membros/{membro_id}")
def editar_membro(request, membro_id: int, data: MembroSchema):
    try:
        membro = Membro.objects.get(id=membro_id)
        for attr, value in data.dict(exclude_unset=True).items():
            if attr != 'id':
                setattr(membro, attr, value)
        
        membro.save()
        return {"message": "Dados atualizados com sucesso"}
    except Membro.DoesNotExist:
        raise HttpError(404, "Membro não encontrado")

# Com o método DELETE. Remove um membro.
@api.delete("/membros/{membro_id}")
def excluir_membro(request, membro_id: int):
    try:
        membro = Membro.objects.get(id=membro_id)
        membro.delete()
        return {"message": "Membro removido com sucesso"}
    except Membro.DoesNotExist:
        raise HttpError(404, "Membro não encontrado")