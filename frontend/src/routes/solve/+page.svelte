<script lang="ts">
	import { goto } from "$app/navigation";
	import { onMount } from "svelte";

  const puzzles = [
    // "1234567890",
    "123456780",
    "281043765",
    "123804765",
    "283645017",
    "876543210"
  ];

  const randomPuzzle = puzzles[Math.floor(Math.random() * puzzles.length)];

  onMount(() => {
    goto(`/solve/${randomPuzzle}`);
  })
</script>