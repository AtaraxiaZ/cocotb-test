from cocotb_test.simulator import run
import pytest
import os

tests_dir = os.path.dirname(__file__)

# For parallel runs
# Pre-compile:
# pytest -m compile test_dff_param.py
# Run:
# pytest --workers 2 test_dff_param.py
# There are possibly better ways to o this

@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")
@pytest.mark.compile
def test_complile():
    run(
        verilog_sources=[os.path.join(tests_dir, "dff.v")],
        toplevel="dff_test",
        module="dff_cocotb",
        compile_only=True,
    )


@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")
@pytest.mark.parametrize("seed", range(6))
def test_dff_verilog_param(seed):
    run(
        verilog_sources=[os.path.join(tests_dir, "dff.v")],
        toplevel="dff_test",
        module="dff_cocotb",
        seed=seed,
    )


@pytest.mark.skipif(os.getenv("SIM") == "ghdl", reason="Verilog not suported")
@pytest.mark.parametrize("testcase", ["run_test_001", "run_test_001"])
def test_dff_verilog_testcase(testcase):
    run(
        verilog_sources=[os.path.join(tests_dir, "dff.v")],
        toplevel="dff_test",
        module="dff_cocotb",
        testcase=testcase,
    )


# For GHDL create new build/direcotry for every run
@pytest.mark.skipif(os.getenv("SIM") == "verilator", reason="VHDL not suported")
@pytest.mark.skipif(os.getenv("SIM") == "icarus", reason="VHDL not suported")
@pytest.mark.parametrize("seed", range(8))
def test_dff_vhdl_param(seed):
    run(
        vhdl_sources=[os.path.join(tests_dir, "dff.vhdl")],
        toplevel="dff_test_vhdl",
        module="dff_cocotb",
        toplevel_lang="vhdl",
        seed=seed,
        sim_build="sim_build/"+str(seed)
    )
