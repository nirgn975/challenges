/**
There's a 3 for 2 offer on mangoes. For a given price and quantity, calculate the total cost of the mangoes.
**/

function mango(quantity, price){
  var mango_quantity = Math.floor(quantity / 3);
  return (quantity - mango_quantity) * price
}
