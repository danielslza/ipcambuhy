<template>
  <q-layout view="lHh Lpr lFf">
    
    <!-- HEADER -->
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

        <!-- Espaçamento correto -->
        <q-space />

        <!-- Botão login -->
        <q-btn
          flat
          round
          icon="account_circle"
          :to="{ name: 'login' }"
        >
          <q-tooltip>Acesso Restrito</q-tooltip>
        </q-btn>

      </q-toolbar>
    </q-header>

    <!-- CONTEÚDO -->
    <q-page-container>
      <router-view />
    </q-page-container>

    <!-- FOOTER -->
    <q-footer class="bg-secondary text-white text-center q-pa-sm">
      <span class="text-caption">
        © 2026 IPB - Sistema de Gestão Interna
      </span>
    </q-footer>

  </q-layout>
</template>

<style scoped>
.container {
  max-width: 1200px;
  margin: 0 auto;
  width: 100%;
}

.subtitle {
  margin-top: -6px;
  opacity: 0.85;
}

.line-height-1 {
  line-height: 1;
}

.logo {
  height: 45px;
  width: auto;
  object-fit: contain;
}

.custom-toolbar {
  min-height: 80px; /* padrão é ~50px */
}

.titleipb {
    font-size: 20px; /* Ajustado para dar destaque ao nome da igreja */
    padding-left: 10px;
    font-family: 'ZapfHumanist', sans-serif; 
    font-weight: normal;
    letter-spacing: 0.2px; /* Ajuda na estética da Zapf Humanist */
}
</style>