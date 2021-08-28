<script setup>
import { ref } from 'vue'

defineProps({
  msg: String
})

const count = ref(0)
</script>

<template>
    <h2> Natta </h2>
    <h3> {{test}} </h3>
    <h4> {{description}} </h4>
    <img src="../assets/logo.png">
</template>

<script>
export default {
    data: () => {
        return {
            test : 'HAHAHAHAHAHHA',
            description : 'I am bat man you know?'
        }
    }
}
</script>


<style scoped>
a {
  color: #75e96b;
}
</style>
