use colored::*;
use pyo3::prelude::*;

#[pyfunction]
#[pyo3(signature = (message, color, bg = "None", bold = false, italic = false, underline = false))]
fn say(message: &str, color: &str, bg: Option<&str>, bold: bool, italic: bool, underline: bool) -> PyResult<String> {
    let mut colored_message = message.color(parse_color(color));

    if let Some(bg_color) = bg {
        colored_message = colored_message.on_color(parse_color(bg_color));
    }

    if bold {
        colored_message = colored_message.bold();
    }

    if italic {
        colored_message = colored_message.italic();
    }

    if underline {
        colored_message = colored_message.underline();
    }

    Ok(colored_message.to_string())
}

#[pyfunction]
#[pyo3(signature = (items, color, bg = "None", bold = false, italic = false, underline = false))]
fn list(items: Vec<String>, color: &str, bg: Option<&str>, bold: bool, italic: bool, underline: bool) -> PyResult<Vec<String>> {
    let colored_items = items
        .into_iter()
        .map(|item| {
            let mut colored_item = item.color(parse_color(color));

            if let Some(bg_color) = bg {
                colored_item = colored_item.on_color(parse_color(bg_color));
            }

            if bold {
                colored_item = colored_item.bold();
            }

            if italic {
                colored_item = colored_item.italic();
            }

            if underline {
                colored_item = colored_item.underline();
            }

            colored_item.to_string()
        })
        .collect();

    Ok(colored_items)
}

fn parse_color(color: &str) -> Color {
    match color {
        "black" => Color::Black,
        "red" => Color::Red,
        "green" => Color::Green,
        "yellow" => Color::Yellow,
        "blue" => Color::Blue,
        "magenta" | "purple" => Color::Magenta,
        "cyan" => Color::Cyan,
        "white" => Color::White,
        "bright_black" => Color::BrightBlack,
        "bright_red" => Color::BrightRed,
        "bright_green" => Color::BrightGreen,
        "bright_yellow" => Color::BrightYellow,
        "bright_blue" => Color::BrightBlue,
        "bright_magenta" => Color::BrightMagenta,
        "bright_cyan" => Color::BrightCyan,
        "bright_white" => Color::BrightWhite,
        _ => {
            if let Some((r, g, b)) = parse_rgb(color) {
                Color::TrueColor { r, g, b }
            } else {
                Color::White
            }
        }
    }
}

fn parse_rgb(color: &str) -> Option<(u8, u8, u8)> {
    if color.starts_with("rgb(") && color.ends_with(")") {
        let rgb: Vec<&str> = color[4..color.len() - 1].split(',').collect();
        if rgb.len() == 3 {
            let r = rgb[0].trim().parse().ok()?;
            let g = rgb[1].trim().parse().ok()?;
            let b = rgb[2].trim().parse().ok()?;
            Some((r, g, b))
        } else {
            None
        }
    } else {
        None
    }
}

#[pymodule]
fn hpyrust_text(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(say, m)?)?;
    m.add_function(wrap_pyfunction!(list, m)?)?;
    Ok(())
}