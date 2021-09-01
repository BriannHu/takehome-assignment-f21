<template>
  <div id="main">
    <p>I've been clicked {{ count }} times</p>
    <b-button v-on:click="count += 1" variant="success">Add 1</b-button>
    <b-button v-on:click="count -= 1" variant="danger">Minus 1</b-button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: this.episodes_seen ? this.episodes_seen : 0 // otherwise /count route will have NaN error
    };
  },
  props: { episodes_seen: Number }
};
</script>

<style></style>
