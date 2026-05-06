#include <strings/ascii.hpp>
#include <strings/builder.hpp>
#include <strings/charconv_stubs.hpp>
#include <strings/codec.hpp>
#include <strings/codepoint_stringers.hpp>
#include <strings/codepoint.hpp>
#include <strings/compare.hpp>
#include <strings/decimal_digits.hpp>
#include <strings/fold_simple.hpp>
#include <strings/fold.hpp>
#include <strings/format_locale.hpp>
#include <strings/format_spec.hpp>
#include <strings/format.hpp>
#include <strings/fp.hpp>
#include <strings/join.hpp>
#include <strings/marshal_traits.hpp>
#include <strings/replace.hpp>
#include <strings/search_folded.hpp>
#include <strings/split.hpp>
#include <strings/string_traits.hpp>
#include <strings/trim.hpp>
#include <strings/utf.hpp>

int main() {
    return strings::ascii::is_upper_alpha('A') ? 0 : 1;
}
