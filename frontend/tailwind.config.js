/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {
      colors : {
        "dark-purple" : "#160c28ff",
        "honeydew" : "#e1efe6ff",
        "naples-yellow" : "#efcb68ff",
        "ash-gray" : "#aeb7b3ff",
        "linen" : "#FAF9F7"
      }
    },
    fontFamily: {
      "montserrat": ["Montserrat", "sans-serif"]
    },
  },
  plugins: [],
}

// montserrat