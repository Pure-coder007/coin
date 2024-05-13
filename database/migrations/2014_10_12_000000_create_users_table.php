<?php

use Illuminate\Support\Facades\Schema;
use Illuminate\Support\Facades\DB;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('users', function (Blueprint $table) {
            $table->id();
            $table->string('name');
            $table->string('email_address')->unique();
            $table->string('password');
            $table->string('Occupation');
            $table->string('DOB');
            $table->string('Residential_address');
            $table->string('Country');
            $table->bigInteger('mobile_no')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->bigInteger('Account_wallet')->default(0);
            $table->ipAddress('ip_address')->default(request()->ip());
            $table->timestamp('Registeration Date')->default(DB::raw('CURRENT_TIMESTAMP'));
            $table->bigInteger('Net_Profits')->default(0);
            $table->bigInteger('Bonus_Profits')->default(0);
            $table->bigInteger('Available_total')->default(0);
            $table->string('role')->default('user'); // Add a role column with 'user' as the default
            $table->rememberToken();
            $table->timestamps();
        });
        DB::unprepared('
            CREATE TRIGGER update_Net_Profits
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.bonus_profits IS NULL THEN
        SET NEW.Net_Profits = NEW.Bonus_Profits;
    ELSE
        SET NEW.Net_Profits = NEW.Bonus_Profits + OLD.Bonus_Profits;
    END IF;
END;
        ');
    }

    /**
     * Reverse the migrations.
     * SET NEW.Net_Profits = NEW.Bonus_Profits + (NEW.Net_Profits - OLD.Bonus_Profits);
     * php artisan db:seed --class=AdminUserSeeder
     */
    public function down(): void
    {
        Schema::dropIfExists('users');


        // Drop the trigger when rolling back the migration
        DB::unprepared('DROP TRIGGER IF EXISTS update_net_profits');
    }

    // public function isAdmin()
    // {
    //     return $this->role === 'admin';
    // }
};
