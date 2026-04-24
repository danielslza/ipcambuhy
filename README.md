# 🏛️ Sistema de Gestão de Membros - IPB Cambuhy

Sistema web desenvolvido para gerenciamento interno de membros da Igreja Presbiteriana do Cambuhy.

O projeto conta com:

* Backend em **Django + Django Ninja**
* Frontend em **Vue 3 + Quasar Framework**
* Comunicação via API REST

---

## 🚀 Funcionalidades

### 🔐 Autenticação

* Login de usuários (baseado no Django Auth)
* Controle de acesso à área administrativa (frontend)

### 👥 Gestão de Membros

* Cadastro de novos membros
* Listagem completa
* Edição de dados
* Exclusão de membros
* Identificação de membros da liderança

### 🌐 Área Pública

* Página institucional da igreja
* Exibição de horários de culto
* Mapa com localização

---

## 🧱 Tecnologias utilizadas

### Backend

* Python
* Django
* Django Ninja
* SQLite (ambiente de desenvolvimento)

### Frontend

* Vue 3
* Quasar Framework
* Axios
* Pinia (estrutura preparada)
* Leaflet (mapa)

---

## 📁 Estrutura do Projeto

```
sistema-ipb/
│
├── backend/
│   ├── core/              # Configurações do Django
│   ├── membros/           # App principal (modelos e API)
│   └── db.sqlite3
│
├── frontend/
│   ├── src/
│   │   ├── pages/         # Páginas (Login, Admin, Home)
│   │   ├── layouts/       # Layouts (público e admin)
│   │   ├── components/    # Componentes reutilizáveis
│   │   └── router/        # Rotas
│   └── quasar.config.js
│
└── README.md
```

---

## ⚙️ Como rodar o projeto

### 🔧 Backend (Django)

```bash
# entrar na pasta do backend
cd backend

# criar ambiente virtual
python -m venv venv

# ativar (Windows)
venv\Scripts\activate

# instalar dependências
pip install -r requirements.txt

# rodar migrations
python manage.py migrate

# criar superusuário (opcional)
python manage.py createsuperuser

# rodar servidor
python manage.py runserver
```

Backend disponível em:

```
http://localhost:8000
```

---

### 🎨 Frontend (Quasar)

```bash
# entrar na pasta frontend
cd frontend

# instalar dependências
npm install

# rodar projeto
npm run dev
```

Frontend disponível em:

```
http://localhost:9000
```

---

## 🔗 Rotas principais

### 🌐 Frontend

| Rota     | Descrição             |
| -------- | --------------------- |
| `/`      | Página inicial        |
| `/login` | Tela de login         |
| `/admin` | Painel administrativo |

---

### 🔧 API (Backend)

| Método | Rota                | Descrição        |
| ------ | ------------------- | ---------------- |
| POST   | `/api/login`        | Autenticação     |
| GET    | `/api/membros`      | Listar membros   |
| POST   | `/api/membros`      | Criar membro     |
| PATCH  | `/api/membros/{id}` | Atualizar membro |
| DELETE | `/api/membros/{id}` | Excluir membro   |

---

## ⚠️ Observações importantes

* O sistema utiliza um **token temporário (simulado)** para autenticação.
* As rotas da API **ainda não possuem proteção real**.
* O banco atual é SQLite, recomendado apenas para desenvolvimento.

---

## 🔒 Melhorias futuras

* Implementação de autenticação real (JWT)
* Controle de permissões no backend
* Integração com PostgreSQL
* Validação de dados mais robusta
* Proteção das rotas administrativas
* Deploy em ambiente de produção

---

## 📌 Status do projeto

🚧 Em desenvolvimento — versão inicial funcional

---

## 👨‍💻 Autor

Desenvolvido por **Daniel**. Projeto com fins de aprendizado.

---

## 📄 Licença

Este projeto é livre para uso e modificação.
