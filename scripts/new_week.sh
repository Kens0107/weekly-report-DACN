#!/usr/bin/env bash
# Quickly scaffold a new weekly report folder from the base template.
# macOS/Linux equivalent of new_week.ps1.
#
# Usage: ./scripts/new_week.sh 3

set -euo pipefail

if [[ $# -ne 1 || ! "$1" =~ ^[0-9]+$ ]]; then
    echo "Usage: $0 <week-number>" >&2
    exit 1
fi

week_number=$((10#$1))
week_str=$(printf "%02d" "$week_number")
root_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
template_dir="$root_dir/template"
target_dir="$root_dir/reports/week-$week_str"

if [[ -e "$target_dir" ]]; then
    echo "Warning: Directory $target_dir already exists!" >&2
    exit 1
fi

echo "Scaffolding weekly report for Week $week_number at $target_dir..."

# Copy template files, skipping build artifacts and the full template document
mkdir -p "$target_dir"
rsync -a \
    --exclude='*.aux' --exclude='*.log' --exclude='*.pdf' --exclude='*.out' \
    --exclude='*.synctex.gz' --exclude='*.fdb_latexmk' --exclude='*.fls' \
    --exclude='weekly_report_template.*' \
    "$template_dir/" "$target_dir/"

# Create week-specific figures directory
mkdir -p "$target_dir/figures"

# Update relative style paths in main.tex (going up 2 directories)
if [[ -f "$target_dir/main.tex" ]]; then
    sed -i '' \
        -e 's|\\usepackage{\.\./style/weeklyreport}|\\usepackage{../../style/weeklyreport}|' \
        -e 's|\\input{\.\./style/macros\.tex}|\\input{../../style/macros.tex}|' \
        "$target_dir/main.tex"
fi

# Update week number in config.tex
if [[ -f "$target_dir/config.tex" ]]; then
    sed -i '' -E "s|\\\\newcommand\\{\\\\WeekNo\\}\\{[0-9]+\\}|\\\\newcommand{\\\\WeekNo}{$week_number}|" \
        "$target_dir/config.tex"
fi

echo "Successfully created reports/week-$week_str!"
echo "Open $target_dir/config.tex and files in sections/ to start writing."
