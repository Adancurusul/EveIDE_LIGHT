module tb_test;

reg [8:0] selector;

initial begin
    $from_myhdl(
        selector
    );
end

test dut(
    selector
);

endmodule
