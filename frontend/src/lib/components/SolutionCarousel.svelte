<script lang="ts">
  import emblaCarouselSvelte from 'embla-carousel-svelte'
  import type { EmblaOptionsType, EmblaPluginType, EmblaCarouselType } from 'embla-carousel';
  import { WheelGesturesPlugin } from 'embla-carousel-wheel-gestures'
	import ChevronLeft from 'lucide-svelte/icons/chevron-left';
  import ChevronRight from 'lucide-svelte/icons/chevron-right';
	import PuzzleMatrix from './PuzzleMatrix.svelte';
  

  let options: EmblaOptionsType = { loop: false }
  let plugins: EmblaPluginType[] = [WheelGesturesPlugin()]

  let emblaApi: EmblaCarouselType

  let childrenCount = 0
  let scrollProgress = 0

  function onInit(event: { detail: EmblaCarouselType; }): void {
    emblaApi = event.detail
    scrollProgress = emblaApi.selectedScrollSnap() + 1
    childrenCount = emblaApi.slideNodes().length

    emblaApi.on('select', () => {
      scrollProgress = emblaApi.selectedScrollSnap() + 1
      childrenCount = emblaApi.slideNodes().length

      emblaApi.slideNodes()[scrollProgress - 1].classList.remove('opacity-25')
      emblaApi.slideNodes()[scrollProgress - 1].classList.add('opacity-100')

      emblaApi.slideNodes()[scrollProgress].classList.add('opacity-25')

      if (scrollProgress - 2 >= 0) {
        emblaApi.slideNodes()[scrollProgress - 2].classList.add('opacity-25')
      }

      if (scrollProgress < childrenCount) {
        emblaApi.slideNodes()[scrollProgress].classList.add('opacity-25')
      }

      if (scrollProgress - 1 >= 0) {
        emblaApi.slideNodes()[scrollProgress - 1].classList.remove('opacity-25')
        emblaApi.slideNodes()[scrollProgress - 1].classList.add('opacity-100')
      }
    })
  }
</script>

<div class="w-full max-w-96 bg-embla-carousel p-4 rounded-[.25rem] overflow-hidden">
  <div class="overflow-hidden" use:emblaCarouselSvelte={{ options, plugins }} on:emblaInit={onInit}>
    <div class="flex gap-2">
      <slot />
		</div>
	</div>

  <div class="flex justify-between mt-4">
    <div class="flex gap-2">
      <button class="px-4 py-2 bg-blue-500 text-white rounded-lg" on:click={() => emblaApi.scrollPrev(true)}><ChevronLeft /></button>
      <button class="px-4 py-2 bg-blue-500 text-white rounded-lg" on:click={() => emblaApi.scrollNext(true)}><ChevronRight /></button>
    </div>

    <div class="flex gap-2">
      <p class="text-sm italic">{scrollProgress} of {childrenCount}</p>
    </div>
  </div>
</div>