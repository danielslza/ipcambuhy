<template>
  <q-layout view="lHh Lpr lFf">
    
    <!-- Header -->
    <q-header elevated class="bg-primary text-white">
      <q-toolbar class="custom-toolbar">
        
        <!-- Logo + Nome -->
        <div 
          class="row items-center cursor-pointer"
          @click="$router.push({ name: 'inicio' })"
        >
          <img 
            src="~assets/logo-ipb-branco.png"
            alt="Logo IPB"
            class="logo"
            />

          <div class="column q-ml-sm">
            <span class="titleipb">Igreja Presbiteriana do Cambuhy</span>
          </div>
        </div>

        <q-space />

        <!-- Botão Home -->
        <q-btn 
          flat 
          round 
          dense 
          icon="home"
          color="white"
          :to="{ name: 'inicio' }"
          class="q-mr-sm"
        >
          <q-tooltip>Página Inicial</q-tooltip>
        </q-btn>

        <!-- Logado / Sair? -->
        <q-chip 
          clickable
          :color="hoverLogado ? 'negative' : 'white'" 
          :text-color="hoverLogado ? 'white' : 'primary'" 
          :icon="hoverLogado ? 'logout' : 'verified_user'"
          class="text-weight-medium logado-chip"
          @mouseenter="hoverLogado = true"
          @mouseleave="hoverLogado = false"
          @click="logout"
        >
          {{ hoverLogado ? 'Sair?' : 'Logado' }}
        </q-chip>

      </q-toolbar>
    </q-header>

    <!-- Conteúdo -->
    <q-page-container>
      <router-view />
    </q-page-container>

    <!-- Footer -->
    <q-footer class="bg-secondary text-white text-center q-pa-sm">
      <span class="text-caption">
        © 2026 IPB - Sistema de Gestão Interna
      </span>
    </q-footer>

  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const hoverLogado = ref(false)

// Logout
const logout = () => {
  localStorage.removeItem('token_ipb')
  router.push({ name: 'login' })
}
</script>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.logo {
  height: 45px;
  width: auto;
  object-fit: contain;
}

.custom-toolbar {
  min-height: 80px;
}

.titleipb {
  font-size: 20px;
  padding-left: 10px;
  font-family: 'ZapfHumanist', sans-serif; 
  font-weight: normal;
  letter-spacing: 0.2px;
}

.logado-chip {
  transition: all 0.3s ease;
  cursor: pointer;
  min-width: 90px;
}

.logado-chip :deep(.q-chip__content) {
  justify-content: center;
}
</style>