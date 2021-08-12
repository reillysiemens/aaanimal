mod adjectives;
mod animals;

use adjectives::ADJECTIVES;
use animals::ANIMALS;

use pyo3::prelude::*;
use rand::{rngs::ThreadRng, seq::SliceRandom};

/// Generate mostly unique, friendly names.
///
/// Attributes:
///     __version__ (str): The package version.
#[pymodule]
fn aaanimal(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    // Add the current cargo package version to the Python module.
    m.add("__version__", env!("CARGO_PKG_VERSION"))?;

    /// Generate mostly unique, friendly names.
    ///
    /// Args:
    ///     adjectives (int): The number of adjectives.
    ///     animals (int): The number of animals.
    ///     separator (str): The word separator.
    ///
    /// Returns:
    ///     str: The generated name.
    #[pyfn(m)]
    #[pyo3(
        name = "generate",
        // XXX: 2021-08-11 - Is this text signature correct?
        text_signature = "(adjectives=2, animals=1, separator='-')"
    )]
    fn generate(
        animals: Option<u128>,
        adjectives: Option<u128>,
        separator: Option<&str>,
    ) -> String {
        // XXX: 2021-08-11 - Is there a way to avoid instantiating this on
        // every call? Is that even a good idea?
        let mut rng = ThreadRng::default();
        let mut words = String::new();
        let adjectives = adjectives.unwrap_or(2);
        let animals = animals.unwrap_or(1);
        let separator = separator.unwrap_or("-");

        for count in 0..adjectives {
            let adjective = ADJECTIVES
                .choose(&mut rng)
                .expect("Adjective array was inexplicably empty.");
            words.push_str(adjective);
            if count < adjectives - 1 {
                words.push_str(&separator);
            }
        }

        if adjectives != 0 && animals != 0 {
            words.push_str(&separator);
        }

        for count in 0..animals {
            let animal = ANIMALS
                .choose(&mut rng)
                .expect("Animal array was inexplicably empty.");
            words.push_str(animal);
            if count < animals - 1 {
                words.push_str(&separator);
            }
        }

        words
    }

    Ok(())
}
