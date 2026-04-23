<template>
  <q-item
    clickable
    :to="link"
    active-class="bg-grey-3"
  >
    <q-item-section avatar>
      <q-icon :name="icon" />
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ title }}</q-item-label>
      <q-item-label caption>
        {{ caption }}
      </q-item-label>
    </q-item-section>
  </q-item>
</template>

<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  caption: {
    type: String,
    default: ''
  },
  icon: {
    type: String,
    default: 'link'
  },
  link: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.q-item {
  border-radius: 8px;
  margin: 4px 8px;
}
</style>