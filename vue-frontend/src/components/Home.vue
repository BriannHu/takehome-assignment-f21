<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions complete="complete" />
    <!-- PART 6: User input and submit button -->
    <div class="form-group">
      <input
        :style="inputStyle"
        type="text"
        v-model="currentShowName"
        placeholder="Enter show name"
        required
      />
      <b-button @click="handleClick($event)" title="Add Show" variant="primary">
        Add Show
      </b-button>
    </div>
    <!-- PART 4: Modify the Show component to accept all of these props -->
    <table class="table">
      <thead>
        <tr>
          <th scope="col">Show Name</th>
          <th scope="col">ID</th>
          <th scope="col">Episodes Seen</th>
          <th scope="col">Counter</th>
          <th scope="col">Actions</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <Show
          v-for="show in shows"
          :key="show.id"
          :id="show.id"
          :name="show.name"
          :episodes_seen="show.episodes_seen"
          v-on:delete-row="handleDelete(show)"
        />
      </tbody>
    </table>
  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },
  data() {
    return {
      currentShowName: null,
      inputStyle: {
        border: "1px #007BFF solid",
        borderRadius: "2px",
        height: "2.275rem",
        padding: "10px"
      },
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ]
    };
  },
  methods: {
    handleClick: function(e) {
      if (this.currentShowName === null) {
        alert("Show name cannot be empty :(");
        return;
      }
      if (this.shows.find(e => e.name === this.currentShowName)) {
        alert("This show already exists :(");
        return;
      }
      const newShow = {
        name: this.currentShowName,
        id: this.shows[this.shows.length - 1]["id"] + 1,
        episodes_seen: 0
      };
      this.shows.push(newShow);
      this.currentShowName = null;

      e.preventDefault();
    },
    handleDelete: function(show) {
      this.shows.splice(this.shows.indexOf(show), 1);
    }
  }
};
</script>

<style></style>
