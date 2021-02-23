const express = require('express')
const app = express()
const config = require('./config.json')
const { hostname = 'undefined', port = 'undefined', urls = [] } = config

var store = {}

app.get('/', (req, res) => {
  res.send(
    `alive at http://${hostname}:${port}\n store: ${JSON.stringify(store)}\n my config: ${JSON.stringify(config)}`
  )
})

urls.map(({ url, method, output, input }) => {
  if (url) {
    return
  }
  return app.apply(this, method && 'GET', url, (req, res) => {
    var isFullInput = input.every(({ name = 'undefined', count = 0 }) => {
      store[name] = store[name] ? store[name] + 1 : 1
      return store[name] > count
    })
    if (isFullInput)
      output.map(({ craftTime = 100, count = 'undefined' }) => {
        setTimeout(() => {
          res.status(200)
          res.end()
        }, craftTime)
      })
  })
})

app.listen(port, () => {
  console.log(`Example app listening at http://${hostname}:${port}`)
})
