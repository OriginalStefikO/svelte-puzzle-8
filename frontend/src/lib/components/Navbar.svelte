<script lang="ts">
  import Github from 'lucide-svelte/icons/github'
</script>

<header class="sticky top-0 bg-background w-full flex justify-between items-center px-3 border-b-2 h-20 sm:h-16">
  <a href="/" class="text-text">
    <h1 class="font-bold w-32 min-w-32 sm:w-fit">Puzzle 8</h1>
  </a>
  
  <div class="w-fit flex h-full sm:gap-4">
    <nav class="h-full">
      <ul class="flex h-full">
        <li class="h-full w-fit flex items-center hover:bg-accent hover:bg-opacity-75"><a class="p-3 text-text" href="/">Home</a></li>
        <li class="h-full w-fit flex items-center hover:bg-accent hover:bg-opacity-75"><a class="p-3 text-text" href="/about">About</a></li>
      </ul>
    </nav>

    <a href="https://github.com/OriginalStefikO/svelte-puzzle-8" target="_blank" class="flex items-center justify-center shrink-0">
      <Github class="stroke-accent" />
    </a>
  </div>
</header>