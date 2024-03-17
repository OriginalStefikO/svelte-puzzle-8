<script lang="ts">
  export let puzzleMatrix: number[][] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
  ];
</script>

<div class="flex flex-col gap-1">
  {#each puzzleMatrix as row}
    <div class="flex gap-1">
      {#each row as value}
        {#if value != 0}
          <div class="w-8 h-8 bg-primary bg-opacity-45 rounded-lg flex items-center justify-center">
            <p class="font-bold text-xl">{value}</p>
          </div>
        {:else}
          <div class="w-8 h-8 bg-primary bg-opacity-20 rounded-lg"></div>
        {/if}
      {/each}
    </div>
  {/each}  
</div>