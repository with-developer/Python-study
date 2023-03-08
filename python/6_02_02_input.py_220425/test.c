#include <stdio.h>
int main() {
	int key[30] = { 0x12,0xd6,0x93,0xe3,0xf4,0xdd,0x86,0x33,0x60,0x56,0x25,0xda,0x9b,0x9f,0x9e,0xc9,0x9f,0xf0,0x4c,0xaF,0xc6,0xf5,0x49,0x00 };
	char ans[30] = { 0, };
	int temp;
	int t_temp;
	int c_temp;

	for (int i = 0x20; i <= 0x7e; i++) {
		temp = i << 3;
		t_temp = temp;
		temp = temp >> 8;

		c_temp = temp | t_temp;
		c_temp = c_temp & 0xff;

		ans[0] = i;
		for (int q = 0; q <= 22; q++) {
			c_temp = key[q] ^ c_temp;
			ans[q + 1] = c_temp;
			c_temp = c_temp ^ (q + 1);

			temp = c_temp << 3;
			t_temp = temp;
			temp = temp >> 8;

			c_temp = temp | t_temp;
			c_temp = c_temp & 0xff;
			printf("%s\n", ans);
		}
	}
}