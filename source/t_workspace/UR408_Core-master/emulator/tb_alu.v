module tb_alu;

reg [7:0] ds1;
reg [7:0] ds2;
reg [7:0] imm;
reg bra;
wire branch;
wire [7:0] alu_out;
reg [4:0] alu_signal;

initial begin
    $from_myhdl(
        ds1,
        ds2,
        imm,
        bra,
        alu_signal
    );
    $to_myhdl(
        branch,
        alu_out
    );
end

alu dut(
    ds1,
    ds2,
    imm,
    bra,
    branch,
    alu_out,
    alu_signal
);

endmodule
