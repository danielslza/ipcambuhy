<template>
  <q-page class="bg-grey-2">

    <!-- HERO -->
    <div class="text-center q-pa-xl">
      <h2 class="text-primary text-weight-bold q-my-none">Igreja Presbiteriana do Cambuhy</h2>
      <p class="text-h6 text-secondary q-mt-sm q-mb-none">
        Acompanhe nossas atividades e membros através do nosso sistema.
      </p>
    </div>

    <!-- CONTEÚDO: Horários (esquerda) + Mapa (direita) -->
    <div class="row q-px-lg q-pb-xl q-col-gutter-lg" style="max-width: 1100px; margin: 0 auto;">

      <!-- COLUNA ESQUERDA — Informações -->
      <div class="col-12 col-md-5">
        <q-card class="my-card shadow-4" style="border-radius: 12px;">
          <q-card-section class="bg-primary text-white row items-center">
            <q-icon name="schedule" size="24px" class="q-mr-sm" />
            <span class="text-h6">Horários</span>
          </q-card-section>
          <q-card-section class="q-pa-lg">
            <q-list separator>
              <q-item>
                <q-item-section avatar>
                  <q-icon name="wb_sunny" color="primary" />
                </q-item-section>
                <q-item-section>
                  <q-item-label class="text-weight-bold">Escola Dominical</q-item-label>
                  <q-item-label caption>Domingos às 09h</q-item-label>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section avatar>
                  <q-icon name="nights_stay" color="primary" />
                </q-item-section>
                <q-item-section>
                  <q-item-label class="text-weight-bold">Culto</q-item-label>
                  <q-item-label caption>Domingos às 19h</q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card-section>
        </q-card>
      </div>

      

      <!-- COLUNA DIREITA — Mapa -->
      <div class="col-12 col-md-7">
        <q-card class="shadow-4" style="border-radius: 12px; overflow: hidden;">
          <q-card-section class="bg-primary text-white row items-center q-py-sm">
            <q-icon name="place" size="24px" class="q-mr-sm" />
            <span class="text-h6">Nossa Localização</span>
          </q-card-section>

          <div
            id="map"
            style="height: 280px; width: 100%;"
            @mouseenter="habilitarScroll"
            @mouseleave="desabilitarScroll"
          ></div>

          <q-card-section class="row items-center q-py-sm bg-grey-1">
            <q-icon name="location_on" color="primary" size="20px" class="q-mr-sm" />
            <span class="text-body2 text-secondary">
              R. Geraldo Vicentim, 15 - Jardim Residencial Cambuhy
            </span>
          </q-card-section>
        </q-card>
      </div>

    </div>

  </q-page>
</template>

<script setup>
import { onMounted, onBeforeUnmount } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'

let map = null

const lat = -22.209001903816706
const lng = -47.383056248789764

// SVG do pin personalizado nas cores do site
const pinSvg = `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 36" width="36" height="52">
  <path d="M12 0C5.4 0 0 5.4 0 12c0 9 12 24 12 24s12-15 12-24C24 5.4 18.6 0 12 0z" fill="#0F3C2C"/>
  <circle cx="12" cy="11" r="5" fill="#ffffff"/>
  <circle cx="12" cy="11" r="2.5" fill="#1F7D5B"/>
</svg>
`

const customIcon = L.divIcon({
  html: pinSvg,
  className: 'custom-pin',
  iconSize: [36, 52],
  iconAnchor: [18, 52],
  popupAnchor: [0, -52]
})

const habilitarScroll = () => {
  if (map) map.scrollWheelZoom.enable()
}

const desabilitarScroll = () => {
  if (map) map.scrollWheelZoom.disable()
}

onMounted(() => {
  map = L.map('map', {
    center: [lat, lng],
    zoom: 16,
    zoomControl: true,
    scrollWheelZoom: false
  })

  L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OSM</a> &copy; <a href="https://carto.com/">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 19
  }).addTo(map)

  L.marker([lat, lng], { icon: customIcon })
    .addTo(map)
    .bindPopup(`
      <div style="text-align:center; font-family: sans-serif;">
        <strong style="color:#0F3C2C; font-size:14px;">Igreja Presbiteriana do Cambuhy</strong><br>
        <span style="color:#5C5C5C; font-size:12px;">R. Geraldo Vicentim, 15</span><br>
        <span style="color:#5C5C5C; font-size:12px;">Jardim Residencial Cambuhy</span>
      </div>
    `)

  setTimeout(() => {
    map.invalidateSize()
  }, 200)
})

onBeforeUnmount(() => {
  if (map) {
    map.remove()
    map = null
  }
})
</script>

<style scoped>
.my-card {
  transition: transform 0.2s;
}
.my-card:hover {
  transform: scale(1.02);
}
</style>

<style>
.custom-pin {
  background: transparent !important;
  border: none !important;
}

.leaflet-popup-content-wrapper {
  border-radius: 10px !important;
  box-shadow: 0 4px 16px rgba(15, 60, 44, 0.25) !important;
  border: 2px solid #0F3C2C !important;
}

.leaflet-popup-tip {
  border-top-color: #0F3C2C !important;
  box-shadow: none !important;
}
</style>