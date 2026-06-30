"""Unit tests for shared/cli_grammar.py -- pure string/dict logic, no RNS/LXMF needed."""

import unittest

from cli_grammar import cmd_dict_to_cli, decode_patches, encode_patches, help_text, parse_cli


class RoundTripTests(unittest.TestCase):
    """cmd_dict_to_cli(cmd) -> cli line -> parse_cli(line) reproduces (name, kwargs)."""

    def test_svc_restart(self):
        line, content = cmd_dict_to_cli({"cmd": "svc_restart", "service": "rnsd"})
        self.assertEqual(line, "svc restart rnsd")
        self.assertIsNone(content)
        name, kwargs = parse_cli(line)
        self.assertEqual(name, "svc_restart")
        self.assertEqual(kwargs, {"service": "rnsd"})

    def test_svc_stop_start(self):
        for action in ("stop", "start"):
            line, _ = cmd_dict_to_cli({"cmd": f"svc_{action}", "service": "rbloxx-agent"})
            name, kwargs = parse_cli(line)
            self.assertEqual(name, f"svc_{action}")
            self.assertEqual(kwargs, {"service": "rbloxx-agent"})

    def test_get_config(self):
        line, content = cmd_dict_to_cli({"cmd": "get_config", "type": "rns"})
        self.assertEqual(line, "get config rns")
        self.assertIsNone(content)
        name, kwargs = parse_cli(line)
        self.assertEqual((name, kwargs), ("get_config", {"type": "rns"}))

    def test_get_telemetry(self):
        line, content = cmd_dict_to_cli({"cmd": "get_telemetry"})
        self.assertEqual(line, "get telem")
        self.assertIsNone(content)
        name, kwargs = parse_cli(line)
        self.assertEqual((name, kwargs), ("get_telemetry", {}))

    def test_get_ifstatus(self):
        line, content = cmd_dict_to_cli({"cmd": "get_ifstatus"})
        self.assertEqual(line, "get ifstatus")
        self.assertIsNone(content)
        name, kwargs = parse_cli(line)
        self.assertEqual((name, kwargs), ("get_ifstatus", {}))

    def test_put_config_carries_content(self):
        line, content = cmd_dict_to_cli({"cmd": "put_config", "type": "agent", "content": "hello\nworld"})
        self.assertEqual(line, "put config agent")
        self.assertEqual(content, b"hello\nworld")
        name, kwargs = parse_cli(line)
        self.assertEqual((name, kwargs), ("put_config", {"type": "agent"}))

    def test_patch_config_content_is_plain_text(self):
        patches = [
            {"section": "AutoInterface", "key": "group_id", "value": "rbloxx"},
            {"section": "AutoInterface", "key": "interface_enabled", "value": "True"},
        ]
        line, content = cmd_dict_to_cli({"cmd": "patch_config", "type": "rns", "patches": patches})
        self.assertEqual(line, "patch config rns")
        # Human-readable, not msgpack/binary.
        self.assertEqual(
            content.decode("utf-8"),
            "AutoInterface group_id=rbloxx\nAutoInterface interface_enabled=True",
        )
        self.assertEqual(decode_patches(content), patches)
        name, kwargs = parse_cli(line)
        self.assertEqual((name, kwargs), ("patch_config", {"type": "rns"}))

    def test_patch_config_section_with_dots_in_name(self):
        # Section names can contain dots (e.g. interface hostnames) -- the
        # space delimiter between section and key=value must not break on them.
        patches = [{"section": "rns.beleth.net", "key": "target_port", "value": "4242"}]
        content = encode_patches(patches)
        self.assertEqual(decode_patches(content), patches)

    def test_reboot_default_and_explicit_delay(self):
        line, _ = cmd_dict_to_cli({"cmd": "reboot"})
        self.assertEqual(line, "reboot 5")
        self.assertEqual(parse_cli(line), ("reboot", {"delay_s": 5}))

        line, _ = cmd_dict_to_cli({"cmd": "reboot", "delay_s": 30})
        self.assertEqual(line, "reboot 30")
        self.assertEqual(parse_cli(line), ("reboot", {"delay_s": 30}))

        # Bare verb with no argument at all (zero-token optional-arg form).
        self.assertEqual(parse_cli("reboot"), ("reboot", {"delay_s": 5}))

    def test_shutdown_default_and_explicit_delay(self):
        self.assertEqual(parse_cli("shutdown"), ("shutdown", {"delay_s": 5}))
        self.assertEqual(parse_cli("shutdown 10"), ("shutdown", {"delay_s": 10}))

    def test_wifi_on_off_with_and_without_profile(self):
        line, _ = cmd_dict_to_cli({"cmd": "wifi_set", "enabled": True, "profile": "home"})
        self.assertEqual(line, "wifi on home")
        self.assertEqual(parse_cli(line), ("wifi_set", {"enabled": True, "profile": "home"}))

        line, _ = cmd_dict_to_cli({"cmd": "wifi_set", "enabled": False, "profile": None})
        self.assertEqual(line, "wifi off")
        self.assertEqual(parse_cli(line), ("wifi_set", {"enabled": False, "profile": None}))

    def test_announce(self):
        line, _ = cmd_dict_to_cli({"cmd": "rns_announce"})
        self.assertEqual(line, "announce")
        self.assertEqual(parse_cli(line), ("rns_announce", {}))

    def test_ping(self):
        line, _ = cmd_dict_to_cli({"cmd": "connectivity_check", "dest_hash": "abc123"})
        self.assertEqual(line, "ping abc123")
        self.assertEqual(parse_cli(line), ("connectivity_check", {"dest_hash": "abc123"}))

    def test_log_pull_variants(self):
        self.assertEqual(parse_cli("log pull"), ("log_pull", {"lines": 100, "unit": None}))
        self.assertEqual(parse_cli("log pull 200"), ("log_pull", {"lines": 200, "unit": None}))
        self.assertEqual(parse_cli("log pull 200 rnsd"), ("log_pull", {"lines": 200, "unit": "rnsd"}))

        line, _ = cmd_dict_to_cli({"cmd": "log_pull", "lines": 50, "unit": "rbloxx-agent"})
        self.assertEqual(line, "log pull 50 rbloxx-agent")
        self.assertEqual(parse_cli(line), ("log_pull", {"lines": 50, "unit": "rbloxx-agent"}))

    def test_disk_cleanup(self):
        line, _ = cmd_dict_to_cli({"cmd": "disk_cleanup"})
        self.assertEqual(line, "disk cleanup")
        self.assertEqual(parse_cli(line), ("disk_cleanup", {}))

    def test_agent_update(self):
        line, _ = cmd_dict_to_cli({"cmd": "agent_update"})
        self.assertEqual(line, "agent update")
        self.assertEqual(parse_cli(line), ("agent_update", {}))

    def test_rnode_reset_and_update(self):
        line, _ = cmd_dict_to_cli({"cmd": "rnode_reset", "port": "/dev/ttyUSB0"})
        self.assertEqual(line, "rnode reset /dev/ttyUSB0")
        self.assertEqual(parse_cli(line), ("rnode_reset", {"port": "/dev/ttyUSB0"}))

        line, _ = cmd_dict_to_cli({"cmd": "rnode_update", "port": "/dev/ttyUSB0"})
        self.assertEqual(parse_cli(line), ("rnode_update", {"port": "/dev/ttyUSB0"}))

    def test_shutdown_threshold_maps_onto_set(self):
        line, content = cmd_dict_to_cli({"cmd": "shutdown_threshold", "soc_pct": 20})
        self.assertEqual(line, "set shutdown_threshold=20")
        self.assertIsNone(content)
        self.assertEqual(parse_cli(line), ("set", {"pairs": [("shutdown_threshold", "20")]}))


class SetGrammarTests(unittest.TestCase):
    def test_single_pair_no_spaces(self):
        self.assertEqual(parse_cli("set CR=5"), ("set", {"pairs": [("CR", "5")]}))

    def test_single_pair_with_spaces(self):
        self.assertEqual(parse_cli("set CR = 5"), ("set", {"pairs": [("CR", "5")]}))

    def test_multi_pair_with_spaces(self):
        name, kwargs = parse_cli("set CR = 7 SF = 5 Freq = 896.5")
        self.assertEqual(name, "set")
        self.assertEqual(
            kwargs["pairs"],
            [("CR", "7"), ("SF", "5"), ("Freq", "896.5")],
        )

    def test_multi_pair_no_spaces(self):
        name, kwargs = parse_cli("set CR=7 SF=5 Freq=896.5")
        self.assertEqual(kwargs["pairs"], [("CR", "7"), ("SF", "5"), ("Freq", "896.5")])

    def test_mixed_spacing(self):
        name, kwargs = parse_cli("set CR=7 SF = 5")
        self.assertEqual(kwargs["pairs"], [("CR", "7"), ("SF", "5")])

    def test_no_pairs_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("set")
        with self.assertRaises(ValueError):
            parse_cli("set   ")

    def test_quoted_value_with_spaces(self):
        name, kwargs = parse_cli('set wifi_network="cafa tech"')
        self.assertEqual(kwargs["pairs"], [("wifi_network", "cafa tech")])

    def test_quoted_value_single_quotes(self):
        name, kwargs = parse_cli("set wifi_network='cafa tech'")
        self.assertEqual(kwargs["pairs"], [("wifi_network", "cafa tech")])

    def test_multiple_quoted_and_plain_pairs_one_line(self):
        name, kwargs = parse_cli('set wifi_network="cafa tech" wifi_psk="my password" wifi=on')
        self.assertEqual(
            kwargs["pairs"],
            [("wifi_network", "cafa tech"), ("wifi_psk", "my password"), ("wifi", "on")],
        )

    def test_quoted_value_with_spaces_around_equals(self):
        name, kwargs = parse_cli('set wifi_network = "cafa tech"')
        self.assertEqual(kwargs["pairs"], [("wifi_network", "cafa tech")])

    def test_unclosed_quote_raises(self):
        with self.assertRaises(ValueError):
            parse_cli('set wifi_network="cafa tech')

    def test_bare_key_without_equals_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("set wifi_network")

    def test_key_without_value_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("set wifi_network=")
        with self.assertRaises(ValueError):
            parse_cli("set wifi_network =")


class GetValueGrammarTests(unittest.TestCase):
    def test_get_value(self):
        self.assertEqual(parse_cli("get hostname"), ("get_value", {"key": "hostname"}))
        self.assertEqual(parse_cli("get CR"), ("get_value", {"key": "CR"}))

    def test_get_config_still_works(self):
        self.assertEqual(parse_cli("get config rns"), ("get_config", {"type": "rns"}))

    def test_get_requires_exactly_one_arg(self):
        with self.assertRaises(ValueError):
            parse_cli("get")
        with self.assertRaises(ValueError):
            parse_cli("get a b")


class SetTelUpdateGrammarTests(unittest.TestCase):
    def test_set_tel_update(self):
        self.assertEqual(parse_cli("set tel_update=45"), ("set", {"pairs": [("tel_update", "45")]}))

    def test_get_tel_update(self):
        self.assertEqual(parse_cli("get tel_update"), ("get_value", {"key": "tel_update"}))


class SetSystemKeysGrammarTests(unittest.TestCase):
    def test_set_hostname(self):
        self.assertEqual(parse_cli("set hostname=node42"), ("set", {"pairs": [("hostname", "node42")]}))

    def test_set_clock(self):
        self.assertEqual(parse_cli("set clock=12:00"), ("set", {"pairs": [("clock", "12:00")]}))

    def test_set_date(self):
        self.assertEqual(parse_cli("set date=2026-06-26"), ("set", {"pairs": [("date", "2026-06-26")]}))

    def test_set_mixed_system_and_radio(self):
        name, kwargs = parse_cli("set hostname=node42 CR=7")
        self.assertEqual(kwargs["pairs"], [("hostname", "node42"), ("CR", "7")])


class TrustGrammarTests(unittest.TestCase):
    def test_trust(self):
        self.assertEqual(parse_cli("trust abcdef0123456789"), ("trust", {"hash": "abcdef0123456789"}))

    def test_untrust(self):
        self.assertEqual(parse_cli("untrust abcdef0123456789"), ("untrust", {"hash": "abcdef0123456789"}))

    def test_trust_requires_exactly_one_arg(self):
        with self.assertRaises(ValueError):
            parse_cli("trust")
        with self.assertRaises(ValueError):
            parse_cli("trust a b")


class ReportVerbTests(unittest.TestCase):
    def test_tel_simple(self):
        self.assertEqual(parse_cli("tel cpu_pct=42.3"), ("tel", {"key": "cpu_pct", "value": "42.3"}))

    def test_tel_compound_value_with_commas(self):
        name, kwargs = parse_cli("tel iface.eth0=1024,2048")
        self.assertEqual(name, "tel")
        self.assertEqual(kwargs, {"key": "iface.eth0", "value": "1024,2048"})

    def test_tel_dotted_key(self):
        name, kwargs = parse_cli("tel path.abcd1234=1,RNode,12500,-90,7.5")
        self.assertEqual(kwargs["key"], "path.abcd1234")

    def test_tel_requires_equals(self):
        with self.assertRaises(ValueError):
            parse_cli("tel cpu_pct")

    def test_cfg(self):
        self.assertEqual(parse_cli("cfg rns"), ("cfg", {"type": "rns"}))


class MalformedAndUnknownTests(unittest.TestCase):
    def test_empty_line_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("")
        with self.assertRaises(ValueError):
            parse_cli("   ")

    def test_unknown_verb_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("frobnicate everything")

    def test_svc_wrong_arity_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("svc restart")
        with self.assertRaises(ValueError):
            parse_cli("svc restart a b")

    def test_svc_unknown_action_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("svc frobnicate rnsd")

    def test_wifi_requires_on_or_off(self):
        with self.assertRaises(ValueError):
            parse_cli("wifi maybe")

    def test_wifi_too_many_args_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("wifi on profile extra")

    def test_reboot_too_many_args_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("reboot 5 10")

    def test_ping_requires_one_arg(self):
        with self.assertRaises(ValueError):
            parse_cli("ping")
        with self.assertRaises(ValueError):
            parse_cli("ping a b")

    def test_rnode_unknown_action_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("rnode frobnicate /dev/ttyUSB0")

    def test_cmd_dict_to_cli_unknown_raises(self):
        with self.assertRaises(ValueError):
            cmd_dict_to_cli({"cmd": "does_not_exist"})


class HelpGrammarTests(unittest.TestCase):
    def test_help_bare(self):
        self.assertEqual(parse_cli("help"), ("help", {"topic": None}))

    def test_help_with_topic(self):
        self.assertEqual(parse_cli("help svc"), ("help", {"topic": "svc"}))

    def test_help_too_many_args_raises(self):
        with self.assertRaises(ValueError):
            parse_cli("help svc extra")

    def test_help_text_lists_all_commands_when_no_topic(self):
        text = help_text()
        for verb in ("svc", "set", "trust", "untrust", "reboot", "help"):
            self.assertIn(verb, text)

    def test_help_text_for_known_topic(self):
        self.assertIn("restart|stop|start", help_text("svc"))

    def test_help_text_is_case_insensitive(self):
        self.assertEqual(help_text("SVC"), help_text("svc"))

    def test_help_text_for_unknown_topic(self):
        self.assertIn("no help", help_text("bogus"))


class ShlexQuotingTests(unittest.TestCase):
    def test_service_name_with_spaces_via_quoting(self):
        name, kwargs = parse_cli('svc restart "my service"')
        self.assertEqual(kwargs, {"service": "my service"})


if __name__ == "__main__":
    unittest.main()
