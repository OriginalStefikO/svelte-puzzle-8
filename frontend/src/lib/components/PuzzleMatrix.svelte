<script lang="ts">
	import { puzzleMatrix } from "$lib/stores";

  let currentPuzzleMatrix: number[][];

  puzzleMatrix.subscribe((value) => {
    currentPuzzleMatrix = value;
  })
</script>

<div class="flex flex-col gap-1">
  {#each currentPuzzleMatrix as row}
    <div class="flex gap-1">
      {#each row as value}
        {#if value != 0}
          <div class="w-8 h-8 bg-gray-400 rounded-lg flex items-center justify-center">
            <p class="font-bold text-xl">{value}</p>
          </div>
        {:else}
          <div class="w-8 h-8 bg-gray-300 rounded-lg"></div>
        {/if}
      {/each}
    </div>
  {/each}  
</div>