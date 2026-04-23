from ninja import NinjaAPI, Schema
from .models import Membro
from typing import List, Optional
from django.contrib.auth import authenticate
from ninja.errors import HttpError
from datetime import date

api = NinjaAPI(title="Sistema IPB Cambuhy API")

# --- SCHEMAS ---

class LoginSchema(Schema):
    username: str
    password: str

class MembroSchema(Schema):
    # O ID é opcional para permitir que o POST (criação) funcione sem ele
    id: Optional[int] = None 
    nome: str
    email: Optional[str] = None
    telefone: Optional[str] = None
    data_nascimento: Optional[date] = None
    is_lideranca: bool = False

# --- ROTAS DE AUTENTICAÇÃO ---

@api.post("/login")
def login(request, data: LoginSchema):
    user = authenticate(username=data.username, password=data.password)
    if user:
        # Retorno temporário para o seu localStorage no Quasar
        return {
            "token": "token-temporario-de-teste", 
            "user": {
                "username": user.username, 
                "is_lideranca": user.is_staff
            }
        }
    raise HttpError(401, "Usuário ou senha inválidos")

# --- ROTAS DE MEMBROS (CRUD) ---

@api.get("/membros", response=List[MembroSchema])
def listar_membros(request):
    """Retorna todos os membros cadastrados no banco."""
    return Membro.objects.all()

@api.post("/membros")
def criar_membro(request, data: MembroSchema):
    """Cria um novo membro ignorando o ID enviado pelo front."""
    dados = data.dict(exclude_unset=True)
    dados.pop('id', None)  # Garante que o banco gere o ID automaticamente
    
    membro = Membro.objects.create(**dados)
    return {"id": membro.id, "message": "Membro cadastrado com sucesso"}

@api.patch("/membros/{membro_id}")
def editar_membro(request, membro_id: int, data: MembroSchema):
    """Atualiza apenas os campos enviados no corpo da requisição."""
    try:
        membro = Membro.objects.get(id=membro_id)
        # exclude_unset evita que campos não enviados sobrescrevam dados existentes
        for attr, value in data.dict(exclude_unset=True).items():
            if attr != 'id':  # Segurança: nunca altera a PK
                setattr(membro, attr, value)
        
        membro.save()
        return {"message": "Dados atualizados com sucesso"}
    except Membro.DoesNotExist:
        raise HttpError(404, "Membro não encontrado")

@api.delete("/membros/{membro_id}")
def excluir_membro(request, membro_id: int):
    """Remove o membro permanentemente."""
    try:
        membro = Membro.objects.get(id=membro_id)
        membro.delete()
        return {"message": "Membro removido com sucesso"}
    except Membro.DoesNotExist:
        raise HttpError(404, "Membro não encontrado")