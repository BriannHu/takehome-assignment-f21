<template>
  <!-- PART 4: Add your code here -->
  <!-- display ID to demonstrate unique IDs of newly added shows -->
  <tr>
    <td>
      <b
        ><i>{{ name }}</i></b
      >
    </td>
    <td>{{ id }}</td>
    <td>{{ episodes_seen }}</td>
    <td><Counter v-bind:episodes_seen="episodes_seen" /></td>
    <td>
      <b-button @click="$emit('delete-row')" variant="warning">Delete</b-button>
    </td>
  </tr>
</template>

<script>
// PART 4: Add your code here
import Counter from "./Counter.vue";

export default {
  components: {
    Counter
  },
  props: { id: Number, name: String, episodes_seen: Number }
};
</script>

<style></style>
