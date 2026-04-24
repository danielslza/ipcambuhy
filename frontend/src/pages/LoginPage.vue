<template>
  <q-page class="bg-primary flex flex-center">
    <div class="column items-center">
      
      <img 
        src="~assets/logo-ipb-branco.png" 
        style="width: 120px; margin-bottom: 20px;"
        alt="Logo IPB"
      >

      <q-card class="shadow-24 login-card" style="width: 380px; border-radius: 15px;">
        <q-card-section class="text-center q-pt-lg">
          <div class="text-h5 text-primary text-weight-bold">Acesso Liderança</div>
          <div class="text-caption text-grey-7">Sistema de Gestão Interna</div>
        </q-card-section>

        <q-card-section class="q-px-xl q-pb-lg">
          <q-form @submit="efetuarLogin" class="q-gutter-md">
            <q-input 
              v-model="login.username" 
              label="Usuário" 
              outlined
              dense
              autocomplete="username"
              bg-color="white"
            >
              <template v-slot:prepend>
                <q-icon name="person" color="primary" />
              </template>
            </q-input>

            <q-input 
              v-model="login.password" 
              label="Senha" 
              type="password" 
              outlined
              dense
              autocomplete="current-password"
              @keyup.enter="efetuarLogin"
              bg-color="white"
            >
              <template v-slot:prepend>
                <q-icon name="lock" color="primary" />
              </template>
            </q-input>

            <div class="q-pt-md">
              <q-btn 
                label="Entrar" 
                color="primary" 
                unelevated 
                class="full-width text-weight-bold" 
                size="lg"
                :loading="carregando"
                type="submit"
                style="border-radius: 8px;"
              />
            </div>
          </q-form>
        </q-card-section>

        <q-card-section class="text-center q-pa-none q-pb-md">
          <p class="text-grey-6 text-caption">
            &copy; 2026 Igreja Presbiteriana do Cambuhy
          </p>
        </q-card-section>
      </q-card>
      
      <q-btn flat no-caps label="Esqueci minha senha" color="white" class="q-mt-md" size="sm" />
    </div>
  </q-page>
</template>

<script setup>
import { ref } from 'vue'
import { api } from 'src/boot/axios'
import { useRouter } from 'vue-router'
import { useQuasar } from 'quasar'

const $q = useQuasar()
const router = useRouter()

const carregando = ref(false)

// Dados do formulário.
const login = ref({
  username: '',
  password: ''
})

const efetuarLogin = async () => {
  if (carregando.value) return
  
  carregando.value = true
  try {

    // Chama o backend.
    const response = await api.post('/login', login.value)
    
    $q.notify({ 
      color: 'positive', 
      message: 'Bem-vindo ao sistema!',
      icon: 'check_circle' 
    })
    
    localStorage.setItem('token_ipb', response.data.token)
    router.push({ name: 'painel-admin' })
    
  } catch (error) {
    console.error('Erro no login:', error)
    $q.notify({ 
      color: 'negative', 
      message: 'Usuário ou senha incorretos.',
      icon: 'error'
    })
  } finally {
    carregando.value = false
  }
}
</script>

<style scoped>
.login-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
}
</style>