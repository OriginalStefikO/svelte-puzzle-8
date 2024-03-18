<script lang="ts">
  export let onClick: () => void = () => {};
</script>

<button class="w-fit h-fit bg-blue-500 py-2 px-5 rounded-xl text-white font-bold hover:scale-105" on:click={onClick}>
  <slot />
</button>