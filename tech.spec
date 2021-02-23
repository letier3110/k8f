// ENTITIES

genericBackend {
  type: store || producer || proxy
}

store {
  slots: []
  recipe
  techDetail
}

proxy {
  recipe
  techDetail
}

producer {
  recipe
  techDetail
}

recipe {
  inputs: []
  outputs: []
  processingTime
}

input {
  slot
}

output {
  slot
}

slot {
  resourceType
  count
}

resourceType {
  name
  maxStack?
  img
}

techDetail {
  processingSpeed // 1-2-4 for producers, 15-30-45 for proxy || store
}

// RECIPES

* => void // requester
{
  inputs: anything
  output: nothing
  processingTime: 0
}

<T> => <MxT> // anything as input, anything M times as output - separator, semaphore
<MxT> => <T> // anything M times as input, anything as output - combinator
<T> => <T && !X,X> // anything as input, anything without N and N as output - filter
"iron ore" => "iron plate"
"copper ore" => "copper plate"
"copper plate" => 2 x "wire"
3x"wire" + "iron plate" => "Electronic circuit" // "EC" || "green"

// RESOURCES

"iron ore"
"copper ore"
"copper plate"
"iron plate"
"wire"
"Electronic circuit"


//

filter{
  inputs: anything
  outputs: {
    slot1: anything (without N if present in input)
    slot2: N if present in input
  }
}

combinator: {
  inputs: anything
  outputs: {
    slot1: anything,
    slot2: anything,
    ...
    slotM: anything
  }
}