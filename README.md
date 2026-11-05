# Grocery Value Calculator

**Status: not implemented yet.** The comparison behavior below is the specification. The Python is still to be written.

This is a proof of concept. Working comparisons are the priority. It is undecided whether this becomes a webpage or an application.

The calculation code should stay separate from any interface, so a later webpage or app can call the same functions.

## Scope for now

Weight only: grams, kilograms, ounces, and pounds. Grocery ounces on a package sold by weight are avoirdupois.

Fluid ounces, milliliters, liters, and cups will be added in a later version. Those measure volume, and volume cannot be converted to grams without a density. This project does not judge ingredients or density.

Two items per comparison for now. Price is a number you type, in dollars. There is no currency conversion.

Use only the Python standard library.

## What a comparison does

Each item is a quantity, a unit, and a price. The two items may use different units. You choose the unit used in the result.

Example: item A in pounds, item B in kilograms, result in grams.

For each item:

1. Convert the quantity into one internal unit (grams).
2. Convert that gram amount into the unit requested for the result.
3. Divide by price. That is **units per dollar**.

The better item is the one with more units per dollar. Report both rates, and how much more the better one gives:

```text
(better - worse) / worse * 100
```

If one item yields 11.8 g per dollar and the other yields 10 g per dollar, the first has **18% more quantity per dollar**. If the rates are equal, say so (0%).

Reject a price or quantity that is not greater than zero, and reject a unit this version does not support.

### Avoirdupois factors

- 1 kg = 1000 g
- 1 lb = 453.59237 g
- 1 oz = 28.349523125 g (one pound is 16 ounces)

## Build order

Keep three files so a future webpage or app can import the math without the prompts:

1. `units.py` — `convert(quantity, from_unit, to_unit)`. Accept short names and full words (`g`, `gram`, `grams`, and the same idea for kg, oz, and lb). Convert by going through grams, including when the source and target unit are the same.
2. `compare.py` — given two items and an output unit, return each item's units per dollar, which one is better, and the percent. An item can be a small dict or a `dataclass` with name, quantity, unit, and price. Name is optional for the math.
3. `main.py` — `input()` prompts only. Ask for each item, ask for the output unit, and print both rates and the percent sentence. No conversion math in this file.

Check the work with `assert` before adding a test framework:

- 1 lb and 453.59237 g are the same amount.
- 16 oz equals 1 lb.
- 2 lb at $4 versus 1 lb at $2 are equal value (same units per dollar).
- 2 lb at $4 versus 1 lb at $3: the first has more quantity per dollar. Work the percent by hand and assert that number.
- Price `0` should fail in a way you can see. Unit `"cup"` should also fail for now, because volume units will be added in a later version.
