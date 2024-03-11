import react from '@vitejs/plugin-react';
export default {
  plugins: [react({ jsxRuntime: 'classic' })],
  css: {
    preprocessorOptions: {
      less: {
        math: "always",
        relativeUrls: true,
        javascriptEnabled: true
      },
    },
  },
  appType: "mpa",

} 
