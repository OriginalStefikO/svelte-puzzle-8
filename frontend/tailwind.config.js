/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      colors: {
        'text': '#e8e5ff',
        'background': '#0b0b1e',
        'primary': '#3b82f6',
        'secondary': '#2e2476',
        'accent': '#ff8b38',
       },       
    }
  },
  plugins: []
};